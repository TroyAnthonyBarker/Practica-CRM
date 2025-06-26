import sys
sys.path.insert(0, './src')

from models.user import User
from repositories.user_repository import UserDBManager

class UserService():
    def __init__(self, db_manager: UserDBManager):
        self.db_manager = db_manager
    
    def get_lastest_user(self) -> User:
        return self.db_manager.get_lastest_user()
    
    def get_all_users(self) -> list[User]:
        return self.db_manager.get_all_users()
    
    def search_by_email(self, email: str) -> list[User]:
        return self.db_manager.search_by_email(email)

    def search_by_name(self, name: str) -> list[User]:
        return self.db_manager.search_by_fullname(name)
    
    def register_user(self, name, surname, email, phone_number=None, address=None) -> bool:
        return self.db_manager.register_user(name, surname, email, phone_number, address)