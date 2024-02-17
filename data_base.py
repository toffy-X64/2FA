from config import *
# DataBase MYSQL
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="2fa"
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INT(255) PRIMARY KEY, nickname VARCHAR(255), tg_userid VARCHAR(255), block_account BOOLEAN )")