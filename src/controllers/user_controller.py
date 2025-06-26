import sys
sys.path.insert(0, './src')

from models.user import User
from services.bill_service import BillService
from services.user_service import UserService
from singleton.format import MONEY_FORMAT
from utils import check_email, check_non_optional_string, get_choice


class UserController():
    def __init__(self, user_service: UserService, bill_service: BillService):
        self.user_service = user_service
        self.bill_service = bill_service
    
    def list_users(self) -> str:
        user_list_str = "\n=== LISTA DE USUARIOS ===\n"
        users = self.user_service.get_all_users()

        for i, user in enumerate(users):
            user_list_str += f"\nUsuario #{i + 1}:\n"
            user_list_str += f"{user}\n"
        
        user_list_str += f"\nTotal de usuarios registrados: {len(users)}"

        return user_list_str
    
    def search_user(self) -> list[User]:
        print("""
    === BUSCAR USUARIO ===
    1. Buscar por email
    2. Buscar por nombre
            """)
        choice = get_choice()

        if choice == 1:
            email = input("Ingrese el email del usuario: ")
            users = self.user_service.search_by_email(email)
        elif choice == 2:
            name = input("Ingrese el nombre del usuario: ")
            users = self.user_service.search_by_name(name)
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            return self.search_user()
        
        return users

    def register_user(self)-> User | None:
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

        while not check_email(email):
            print("Email inválido. Por favor, ingrese un email válido.")
            email = input("Ingrese email: ")

        phone_number = input("Ingrese teléfono (opcional): ")
        address = input("Ingrese dirección (opcional): ")

        try:
            if self.user_service.register_user(name, surname, email, phone_number, address):
                return self.user_service.get_lastest_user()
            else:
                return None
        except ValueError as e:
            print(f"Error al registrar usuario: {e}")
            return None
    
    def users_finance_resume(self) -> str:
        users = self.user_service.get_all_users()
        resume = '\n=== RESUMEN FINANCIERO ===\n'

        for user in users:
            user.set_bills(self.bill_service.get_users_bills(user.id))
            resume += f'\n{user.finance_resume()}\n'
        
        total_usuarios = len(users)
        total_facturas = len([bill for user in users for bill in user.bills])
        ingresos_totales = 0
        ingresos_recibidos = 0
        ingresos_pendientes = 0
        
        for user in users:
            ingresos_totales += user.get_monto_total(formated=False)
            ingresos_recibidos += user.get_monto_pagado(formated=False)
            ingresos_pendientes += user.get_monto_pendiente(formated=False)

        resume += "\n--- RESUMEN GENERAL ---\n"
        resume += f"Total usuarios: {total_usuarios}\n"
        resume += f"Total facturas emitidas: {total_facturas}\n"
        resume += f"Ingresos totales: {MONEY_FORMAT.format(ingresos_totales)}\n"
        resume += f"Ingresos recibidos: {MONEY_FORMAT.format(ingresos_recibidos)}\n"
        resume += f"Ingresos pendientes: {MONEY_FORMAT.format(ingresos_pendientes)}\n"

        return resume
    
    def user_bills(self) -> str:
        email = input('Ingrese email del usuario: ')
        print()

        while not check_email(email):
            print('Email no válido, vuelve a introducir.')
            email = input("Ingrese el email del usuario: ")
            print()
        
        try:
            user = self.user_service.search_by_email(email)[0]
        except IndexError:
            print("Usuario no encontrado.")
            return None
        
        user.set_bills(self.bill_service.get_users_bills(user.id))
        
        return user.str_bills()