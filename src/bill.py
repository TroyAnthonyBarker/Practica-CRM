from datetime import datetime

FORMATO_FECHA = "%d/%m/%Y %H:%M"
MONEY_FORMAT = "${:,.2f}"

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

    def get_bill_number(self):
        return self.id
    
    def get_bill_date(self):
        return self.bill_date.strftime(FORMATO_FECHA)
    
    def get_user_id(self):
        return self.user_id
    
    def get_description(self):
        return self.description
    
    def get_monto(self):
        return MONEY_FORMAT.format(self.monto)
    
    def get_state(self):
        return self.state
    
    def __str__(self):
        return f"""Número: {self.id}
Fecha: {self.get_bill_date()}
Descripción: {self.description}
Monto: {self.get_monto()}
Estado: {self.state}"""