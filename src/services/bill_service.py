import sys
sys.path.insert(0, './src')

from models.bill import Bill
from repositories.bill_repository import BillDBManager

class BillService():
    def __init__(self, db_manager: BillDBManager):
        self.db_manager = db_manager
    
    def register_bill(self, user_id, description, monto, status) -> bool:
        return self.db_manager.register_bill(user_id, description, monto, status)
    
    def get_latest_bill(self) -> Bill:
        return self.db_manager.get_latest_bill()
    
    def get_all_bills(self) -> list[Bill]:
        return self.db_manager.get_all_bills()
    
    def get_users_bills(self, user_id) -> list[Bill]:
        return self.db_manager.get_users_bills(user_id)
