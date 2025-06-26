import mysql.connector
import json

conf = json.load(open("./conf/host.json", "r"))

db_connexion_singleton = mysql.connector.connect(
  host=conf["host"],
  port=conf["port"],
  user=conf["user"],
  password=conf["password"],
  database=conf["database"]
)