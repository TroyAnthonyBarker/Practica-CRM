# Practica CRM

Este proyecto es un sistema CRM (Customer Relationship Management) básico, que utiliza Python y SQL para la gestión de usuarios y facturación en una base de datos.

## Estructura del proyecto

```
EJERCICIO_CRM/
│
├── .venv/                  # Entorno virtual (no incluido en el repositorio)
├── conf/
│   └── host.json           # Configuración del host
│
├── db/                     # Lógica y scripts relacionados con la base de datos
│   ├── startup/
│   │   ├── create_db.sql       # Script para creación inicial de la base de datos
│   │   ├── db_creation.py      # Script Python que ejecuta la creación de la DB
│   │   ├── db_inserts.py       # Script Python para insertar datos iniciales
│   │   └── inserts.sql         # Script SQL para insertar datos
│   ├── db_bill.py          # Operaciones sobre las facturas
│   ├── db_manager.py       # Gestión general de la base de datos
│   └── db_user.py          # Operaciones sobre los usuarios
│
├── src/                    # Código fuente de la aplicación
│   ├── bill.py             # Lógica de facturación
│   ├── main.py             # Script principal para ejecutar la aplicación
│   └── user.py             # Lógica relacionada con los usuarios
│
├── Documento_de_Analisis.docx  # Documento de análisis funcional y técnico
```

## Requisitos

- Python 3.8+
- SQLite (u otro motor de base de datos si se adapta)
- Entorno virtual con las dependencias adecuadas

## Instalación

```bash
git clone https://github.com/tu_usuario/EJERCICIO_CRM.git
cd EJERCICIO_CRM
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

> Nota: Necesitaras una Base de Datos MySQL para usar en local puedes usar [XAMPP](https://www.apachefriends.org/es/index.html).

1. Configurar el fichero host.json:

```json
{
  "host": "localhost",
  "port": 3306,
  "user": "<username>",
  "password": "<password>",
  "database": "evolve_scrm"
}
```

2. Crear la base de datos:

```bash
python db/startup/db_creation.py
```

3. Insertar datos iniciales:

```bash
python db/startup/db_inserts.py
```

4. Ejecutar la aplicación:

```bash
python src/main.py
```

## Funcionalidades

- **Gestión de usuarios**: crear, modificar y consultar información de usuarios.
- **Gestión de facturas**: creación y consulta de facturación.
- **Persistencia en base de datos**: mediante scripts SQL y clases Python.

## Autor

- Troy Anthony Barker
- Contacto: troybarker0905@gmail.com

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
