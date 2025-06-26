import sys
sys.path.insert(0, './src')

from services.bill_service import BillService
from services.user_service import UserService
from utils import check_email, get_choice

class BillController():
    def __init__(self, user_service: UserService, bill_service: BillService):
        self.user_service = user_service
        self.bill_service = bill_service
 
    def register_bill(self):
        print("\n=== CREAR DE FACTURA ===")
        user_email = input("Ingrese el email del usuario: ")

        while not check_email(user_email):
            print('Email no válido, vuelve a introducir.')
            user_email = input("Ingrese el email del usuario: ")

        try:
            user = self.user_service.search_by_email(user_email)[0]
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
            if self.bill_service.register_bill(user_id= user.id, description=description, monto=monto_total, status=state):
                return self.bill_service.get_latest_bill()
            else:
                return None

        except ValueError as e:
            print(f"Error al registrar factura: {e}")
            return None