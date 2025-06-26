import sys
sys.path.insert(0, './src')

from repositories.base import DBManager
from mysql.connector import IntegrityError
from models.bill import Bill

class BillDBManager(DBManager):
    def __init__(self, conn):
        super().__init__(conn)

    def register_bill(self, user_id, description, monto, status) -> bool:
        query = "INSERT INTO bills (user_id, description, monto, status_id) VALUES (%s, %s, %s, (SELECT id FROM `bill_status` WHERE status = %s))"
        params = (user_id, description, monto, status)        
        try:
            self.execute_query(query, params)
            self.commit()
            return True
        except IntegrityError as e:
            if e.errno == 1062:
                return False
            else:
                raise
    
    def get_latest_bill(self) -> Bill:
        query = "SELECT b.id, b.bill_date, b.user_id, b.description, b.monto, bs.status " \
        "FROM `bills` b " \
        "LEFT JOIN `bill_status` bs " \
        "ON b.status_id = bs.id "
        "ORDER BY bill_date DESC" \
        "LIMIT 1"

        self.execute_query(query)
        row = self.fetch_one()
        return Bill(*row) if row else None
    
    def get_all_bills(self) -> list[Bill]:
        query = "SELECT b.id, b.bill_date, b.user_id, b.description, b.monto, bs.status " \
        "FROM `bills` b " \
        "LEFT JOIN `bill_status` bs " \
        "ON b.status_id = bs.id "

        self.execute_query(query)
        
        bills = []
        for row in self.fetch_all():
            bills.append(Bill(*row))
        
        return bills
    
    def get_users_bills(self, user_id) -> list[Bill]:
        query = "SELECT b.id, b.bill_date, b.user_id, b.description, b.monto, bs.status " \
        "FROM `bills` b " \
        "INNER JOIN `bill_status` bs " \
        "ON b.status_id = bs.id " \
        "WHERE b.user_id = %s;"

        self.execute_query(query, (user_id,))

        bills = []
        for row in self.fetch_all():
            bills.append(Bill(*row))
        
        return bills