import mysql.connector
import json

conf = json.load(open("./conf/host.json", "r"))

mydb = mysql.connector.connect(
  host=conf["host"],
  port=conf["port"],
  user=conf["user"],
  password=conf["password"],
  database=conf["database"]
)

class DBManager:
  def __init__(self):
    self.connection = mydb
    self.cursor = mydb.cursor()

  def execute_query(self, query, params=None):
    if params:
      self.cursor.execute(query, params)
    else:
      self.cursor.execute(query)

  def fetch_all(self):
    return self.cursor.fetchall()
  
  def fetch_one(self):
    return self.cursor.fetchone()
  
  def commit(self):
    self.connection.commit()

  def close(self):
    self.connection.commit()
    self.cursor.close()
    self.connection.close()