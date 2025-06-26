
# ---------------------------------------------
# ------------- USEFUL FUNCTIONS --------------
# ---------------------------------------------

def get_choice():
    try:
        choice = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return get_choice()
    return choice

def check_non_optional_string(non_optional):
    if len(non_optional) < 3:
        return False
    return True

def check_email(email):
    if "@" not in email or "." not in email:
        return False
    return True