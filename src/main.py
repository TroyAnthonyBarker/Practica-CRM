import sys
sys.path.insert(0, './src')

from singleton.db import db_connexion_singleton as db_conn
from repositories.user_repository import UserDBManager
from repositories.bill_repository import BillDBManager
from services.user_service import UserService
from services.bill_service import BillService
from controllers.user_controller import UserController
from controllers.bill_controller import BillController

from utils import get_choice

user_db_manager = UserDBManager(db_conn)
bill_db_manager = BillDBManager(db_conn)

user_service = UserService(user_db_manager)
bill_service = BillService(bill_db_manager)

user_controller = UserController(user_service, bill_service)
bill_controller = BillController(user_service, bill_service)

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


if __name__ == "__main__":
    option = menu()

    while option != 7:
        if option == 1: # Register User
            new_user = user_controller.register_user()
            if new_user:
                    print("\nUsuario registrado exitosamente!")
                    print(f"ID asignado: {new_user.id}")
                    print(f"Fecha de registro: {new_user.get_registration_date()}")
            else:
                print("\nUsuario no registrado! (Email ya existente.)")

        elif option == 2: # Search User
            users = user_controller.search_user()
            print(f"\n--- USUARIOS ENCONTRADOS ({len(users)}) ---")
            for user in users:
                print(f"\n{user}")

        elif option == 3: # Register Bill
            new_bill = bill_controller.register_bill()
            if new_bill:
                print("\nFactura creada exitosamente!")
                print(new_bill)
            else:
                print("\nFactura no creada. Intentalo de nuevo.")

        elif option == 4: # Show all Users
            print(user_controller.list_users())
            
        elif option == 5: # Show User Bills
            print(user_controller.user_bills())

        elif option == 6: # Resume Users Finences
            print(user_controller.users_finance_resume())

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        option = menu()