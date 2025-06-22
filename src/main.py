import sys
sys.path.insert(0, '.')

from db.db_user import DBUser
from db.db_bill import DBBill

db_user = DBUser()
db_bill = DBBill()

MONEY_FORMAT = "${:,.2f}"

# ---------------------------------------------
# ------------- USEFUL FUNCTIONS --------------
# ---------------------------------------------

def get_choice():
    try:
        choice = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return get_choice()
    return choice

def check_non_optional_string(non_optional):
    if len(non_optional) < 3:
        return False
    return True

def chek_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

# ---------------------------------------------
# ------------------- MENU --------------------
# ---------------------------------------------

def menu():
    print("""
=== SISTEMA CRM ===
1. Registrar nuevo usuario
2. Buscar usuario
3. Crear factura para usuario
4. Mostrar todos los usuarios
5. Mostrar facturas de un usuario
6. Resumen financiero por usuario
7. Salir
""")
    
    return get_choice()

# ---------------------------------------------
# ------------- USER REGISTRATION -------------
# ---------------------------------------------

def register_user():
    print("\n=== REGISTRO DE NUEVO USUARIO ===")
    name = input("Ingrese nombre: ")

    while not check_non_optional_string(name):
        print("Nombre inválido. Por favor, ingrese un nombre válido.")
        name = input("Ingrese nombre: ")

    surname = input("Ingrese apellidos: ")

    while not check_non_optional_string(surname):
        print("Apellidos inválido. Por favor, ingrese un/unos apellidos válido.")
        surname = input("Ingrese apellidos: ")

    email = input("Ingrese email: ")

    while not chek_email(email):
        print("Email inválido. Por favor, ingrese un email válido.")
        email = input("Ingrese email: ")

    phone_number = input("Ingrese teléfono (opcional): ")
    address = input("Ingrese dirección (opcional): ")

    try:
        if db_user.register_user(name, surname, email, phone_number, address):
            return db_user.get_lastest_user()
        else:
            return None
    except ValueError as e:
        print(f"Error al registrar usuario: {e}")
        return None

# ---------------------------------------------
# ------------- USER SEARCHING ----------------
# ---------------------------------------------

def search_by_email(email):
    return db_user.search_by_email(email)


def search_by_name(name):
    return db_user.search_by_fullname(name)

def search_user():
    print("""
=== BUSCAR USUARIO ===
1. Buscar por email
2. Buscar por nombre
          """)
    choice = get_choice()

    if choice == 1:
        email = input("Ingrese el email del usuario: ")
        user = search_by_email(email)
    elif choice == 2:
        name = input("Ingrese el nombre del usuario: ")
        user = search_by_name(name)
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return search_user()
    
    return user

# ---------------------------------------------
# ------------ BILL REGISTRATION --------------
# ---------------------------------------------

def register_bill():
    print("\n=== CREAR DE FACTURA ===")
    user_email = input("Ingrese el email del usuario: ")

    while not chek_email(user_email):
        print('Email no válido, vuelve a introducir.')
        user_email = input("Ingrese el email del usuario: ")

    try:
        user = search_by_email(user_email)[0]
    except IndexError:
        print("Usuario no encontrado.")
        return None
    
    print(f"\nUsuario encontrado: {user.get_full_name()}")
    print()
    
    description = input("Ingrese descripción del servicio/producto: ")
    try:
        monto_total = float(input("Ingrese monto total: "))
        if monto_total < 0:
            print("Monto inválido. Por favor, ingrese un número positivo.")
            return None
    except ValueError:
        print("Monto inválido. Por favor, ingrese un número válido.")
        return None
    
    print("Seleccione el estado de la factura:")
    print("1. Pendiente")
    print("2. Pagada")
    print("3. Cancelada")
    state_choice = get_choice()

    if state_choice == 1:
        state = 'Pendiente'
    elif state_choice == 2:
        state = 'Pagada'
    elif state_choice == 3:
        state = 'Cancelada'
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return None
    
    try:
        if db_bill.register_bill(user_id= user.get_id(), description=description, monto=monto_total, status=state):
            return db_bill.get_latest_bill()
        else:
            return None

    except ValueError as e:
        print(f"Error al registrar factura: {e}")
        return None

# ---------------------------------------------
# -------------- SHOW USERS -------------------
# ---------------------------------------------

def show_users():  
    print("\n=== LISTA DE USUARIOS ===")
    users = db_user.get_all_users()
    for i, user in enumerate(users):
        print(f"\nUsuario #{i + 1}:")
        print(user)
    
    print(f"Total de usuarios registrados: {len(users)}")

# ---------------------------------------------
# ------------ SHOW USER BILLS ----------------
# ---------------------------------------------

def show_user_bills():
    email = input('Ingrese email del usuario: ')
    print()

    while not chek_email(email):
        print('Email no válido, vuelve a introducir.')
        email = input("Ingrese el email del usuario: ")
        print()
    
    try:
        user = search_by_email(email)[0]
    except IndexError:
        print("Usuario no encontrado.")
        return None
    
    for bill in db_bill.get_users_bills(user.get_id()):
        user.add_bill(bill)
    
    print(user.get_string_bills())

# ---------------------------------------------
# ------------ SHOW USER BILLS ----------------
# ---------------------------------------------

def show_user_finance_resume():
    users = db_user.get_all_users()

    print('\n=== RESUMEN FINANCIERO ===')

    for user in users:
        for bill in db_bill.get_users_bills(user.get_id()):
            user.add_bill(bill)
        print('\n' + user.finance_resume())
    
    total_usuarios = len(users)
    total_facturas = len([bill for user in users for bill in user.bills])
    ingresos_totales = 0
    ingresos_recibidos = 0
    ingresos_pendientes = 0
    for user in users:
        ingresos_totales += user.get_monto_total(formated=False)
        ingresos_recibidos += user.get_monto_pagado(formated=False)
        ingresos_pendientes += user.get_monto_pendiente(formated=False)

    print("\n--- RESUMEN GENERAL ---")
    print(f"Total usuarios: {total_usuarios}")
    print(f"Total facturas emitidas: {total_facturas}")
    print(f"Ingresos totales: {MONEY_FORMAT.format(ingresos_totales)}")
    print(f"Ingresos recibidos: {MONEY_FORMAT.format(ingresos_recibidos)}")
    print(f"Ingresos pendientes: {MONEY_FORMAT.format(ingresos_pendientes)}")

# main.py
if __name__ == "__main__":
    option = menu()

    while option != 7:
        if option == 1:
            new_user = register_user()
            if new_user:
                    print("\nUsuario registrado exitosamente!")
                    print(f"ID asignado: {new_user.get_id()}")
                    print(f"Fecha de registro: {new_user.get_registration_date()}")
            else:
                print("\nUsuario no registrado! (Email ya existente.)")

        elif option == 2:
            users = search_user()
            print("\n--- USUARIOS ENCONTRADOS ---")
            for user in users:
                print(user)

        elif option == 3:
            new_bill = register_bill()
            if new_bill:
                print("\nFactura creada exitosamente!")
                print(new_bill)
            else:
                print("\nFactura no creada. Intentalo de nuevo.")

        elif option == 4:
            show_users()
            
        elif option == 5:
            show_user_bills()

        elif option == 6:
            show_user_finance_resume()

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        option = menu()