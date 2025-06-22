import sys
sys.path.insert(0, '.')

from mysql.connector import IntegrityError

from src.user import User
from db.db_manager import DBManager

class DBUser(DBManager):
    def __init__(self):
        super().__init__()

    def register_user(self, name, surname, email, phone_number=None, address=None) -> bool:
        query = "INSERT INTO users (name, surname, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
        params = (name, surname, email, phone_number, address)        
        try:
            self.execute_query(query, params)
            self.commit()
            return True
        except IntegrityError as e:
            if e.errno == 1062:
                return False
            else:
                raise
        
    def get_lastest_user(self) -> User:
        query = "SELECT * FROM users ORDER BY registration_date DESC LIMIT 1"
        self.execute_query(query)
        row = self.fetch_one()
        return User(*row) if row else None

    def search_by_email(self, email) -> list[User]:
        query = f"SELECT * FROM users WHERE LOWER(email) LIKE LOWER('%{email}%')"
        self.execute_query(query)
        users = []
        for row in self.fetch_all():
            users.append(User(*row))
        return users

    def search_by_fullname(self, name) -> list[User]:
        query = f"SELECT * FROM users WHERE LOWER(CONCAT(name, ' ', surname)) LIKE LOWER('%{name}%')"
        self.execute_query(query)
        users = []
        for row in self.fetch_all():
            users.append(User(*row))
        return users
    
    def get_all_users(self) -> list[User]:
        query = "SELECT * FROM `users`;"
        self.execute_query(query)
        users = []
        for row in self.fetch_all():
            users.append(User(*row))
        return users
