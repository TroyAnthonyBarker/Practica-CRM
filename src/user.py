import sys
sys.path.insert(0, '.')

from datetime import datetime
from src.bill import Bill

FORMATO_FECHA = "%d/%m/%Y"
MONEY_FORMAT = "${:,.2f}"

class User:
    def __init__(self, id, name, surname, email, phone_number, address, registration_date: datetime):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.registration_date = registration_date
        self.bills: list[Bill] = []
    
    def get_id(self):
        return self.id
    
    def get_registration_date(self):
        return self.registration_date.strftime(FORMATO_FECHA)
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def get_name(self):
        return self.name
    
    def get_surname(self):  
        return self.surname
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number if self.phone_number else "No especificado"
    
    def get_address(self):
        return self.address if self.address else "No especificado"
    
    def add_bill(self, bill: Bill):
        self.bills.append(bill)
    
    def get_monto_total(self, formated=True) -> str | float:
        monto_total = 0
        for bill in self.bills:
            monto_total += bill.monto
        if formated:
            return MONEY_FORMAT.format(monto_total)
        else:
            return monto_total
    
    def get_monto_pendiente(self, formated=True) -> str | float:
        monto_pendiente = 0
        for bill in self.bills:
            if bill.state == 'Pendiente':
                monto_pendiente += bill.monto
        if formated:
            return MONEY_FORMAT.format(monto_pendiente)
        else:
            return monto_pendiente
    
    def get_monto_pagado(self, formated=True) -> str | float:
        monto_pagado = 0
        for bill in self.bills:
            if bill.state == 'Pagada':
                monto_pagado += bill.monto
        if formated:
            return MONEY_FORMAT.format(monto_pagado)
        else:
            return monto_pagado
    
    def __str__(self):
        return f"ID: {self.id}" \
        f"\nNombre: {self.get_full_name()}" \
        f"\nEmail: {self.email}" \
        f"\nTeléfono: {self.get_phone_number()}" \
        f"\nDirrección: {self.get_address()}" \
        f"\nFecha de registro: {self.get_registration_date()}"
    
    def finance_resume(self):
        return f"Usuario: {self.get_full_name()} ({self.get_email()})" \
        f"\n- Total facturas: {len(self.bills)}" \
        f"\n- Monto total: {self.get_monto_total()}" \
        f"\n- Facturas pagadas: {self.get_monto_pagado()}" \
        f"\n- Facturas pendientes: {self.get_monto_pendiente()}"
    
    def get_string_bills(self):
        bills_txt = f"--- FACTURAS DE {self.get_full_name()} ---\n"

        for i, bill in enumerate(self.bills):
            bills_txt += f"\nFactura #{i+1}:\n{bill.__str__()}\n"
        
        bills_txt += f"\nTotal de facturas: {len(self.bills)}\n"
        bills_txt += f"Monto total facturado: {self.get_monto_total()}\n"
        bills_txt += f"Monto pendiente: {self.get_monto_pendiente()}"
            
        return bills_txt