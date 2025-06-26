# Practica CRM

Este proyecto es un sistema CRM (Customer Relationship Management) básico, que utiliza Python y SQL para la gestión de usuarios y facturación en una base de datos.

## Estructura del proyecto

```
PRACTICA_CRM/
│
├── .venv/
├── conf/
│   └── host.json
│
├── db/
│   └── startup/
│       ├── create_db.sql
│       ├── db_creation.py
│       ├── db_inserts.py
│       └── inserts.sql
│
├── src/
│   ├── controllers
│   │   ├── bill_controller.py  
│   │   └── user_controller.py
│   │
│   ├── models
│   │   ├── bill.py
│   │   └── user.py
│   │
│   ├── repositories
│   │   ├── base.py
│   │   ├── bill_repository.py
│   │   └── user_repository.py
│   │
│   ├── services
│   │   ├── bill_service.py
│   │   └── user_service.py
│   │
│   ├── singleton
│   │   ├── db.py
│   │   └── format.py
│   │
│   ├── main.py
│   └── utils.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.8+
- SQLite (u otro motor de base de datos si se adapta)
- Entorno virtual con las dependencias adecuadas

## Instalación

### Clonación de Repositorio

```bash
git clone https://github.com/tu_usuario/EJERCICIO_CRM.git
cd EJERCICIO_CRM
```

### Creación de entorno virtual de python

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### Instalación de dependencias

```bash
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
