import sys
sys.path.insert(0, './src')

from datetime import datetime
from singleton.format import DATE_FORMAT, MONEY_FORMAT

class Bill:
    def __init__(self, id, bill_date: datetime, user_id, description, monto, state='Pendiente'):

        if state not in ['Pendiente', 'Pagada', 'Cancelada']:
            raise ValueError("Estado debe ser 'Pendiente', 'Pagada' o 'Cancelada'")
        
        self.id = id
        self.bill_date = bill_date
        self.user_id = user_id
        self.description = description
        self.monto = monto
        self.state = state
    
    def get_bill_date(self):
        return self.bill_date.strftime(DATE_FORMAT)
    
    def get_monto(self):
        return MONEY_FORMAT.format(self.monto)
    
    def __str__(self):
        return f"Número: {self.id}\n" \
            f"Fecha: {self.get_bill_date()}\n" \
            f"Descripción: {self.description}\n" \
            f"Monto: {self.get_monto()}\n" \
            f"Estado: {self.state}" 