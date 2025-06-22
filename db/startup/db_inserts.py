import mysql.connector
import json

conf = json.load(open("./conf/host.json", "r"))

mydb = mysql.connector.connect(
    host=conf["host"],
    port=conf["port"],
    user=conf["user"],
    password=conf["password"],
    database="evolve_scrm"
)

mycursor = mydb.cursor()

# Insertar bill_status
mycursor.executemany(
    "INSERT INTO bill_status (status) VALUES (%s)",
    [
        ("Pendiente",),
        ("Pagada",),
        ("Cancelada",)
    ]
)

# Insertar users
mycursor.execute(
    "INSERT INTO users (name, surname, email) VALUES (%s, %s, %s)",
    ("John", "Doe", "j.doe@gmail.com")
)
mycursor.execute(
    "INSERT INTO users (name, surname, email) VALUES (%s, %s, %s)",
    ("Diana", "Miller", "d.miller@hotmail.com")
)
mycursor.execute(
    "INSERT INTO users (name, surname, email, phone, address) VALUES (%s, %s, %s, %s, %s)",
    ("Jane", "Smith", "j.smith@hotmail.com", "123-456-7890", "123 Elm St, Springfield")
)
mycursor.execute(
    "INSERT INTO users (name, surname, email, phone, address) VALUES (%s, %s, %s, %s, %s)",
    ("Alice", "Johnson", "a.johnson@yahoo.com", "987-654-3210", "456 Oak St, Springfield")
)
mycursor.execute(
    "INSERT INTO users (name, surname, email, address) VALUES (%s, %s, %s, %s)",
    ("Bob", "Brown", "b.brown@googlemail.com", "789 Pine St, Springfield")
)
mycursor.execute(
    "INSERT INTO users (name, surname, email, phone) VALUES (%s, %s, %s, %s)",
    ("Charlie", "Davis", "c.davis@gmail.com", "555-123-4567")
)

# Insertar bills
mycursor.executemany(
    "INSERT INTO bills (user_id, description, status_id, monto) VALUES (%s, %s, %s, %s)",
    [
        ('USR001', "Servicio de internet", 1, 59.99),
        ('USR001', "Servicio de internet", 1, 59.99),
        ('USR001', "Servicio de internet", 1, 59.99),
        ('USR002', "Factura de electricidad", 2, 120.50),
        ('USR003', "Pago de agua", 1, 45.00),
        ('USR004', "Suscripción mensual de software", 3, 15.00),
        ('USR005', "Mantenimiento de equipo", 1, 75.00),
        ('USR006', "Compra de suministros de oficina", 2, 30.00)
    ]
)

mydb.commit()
mycursor.close()
mydb.close()