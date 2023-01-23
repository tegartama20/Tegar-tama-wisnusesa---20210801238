import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="bahasa_pemprograman"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("wisnu", "ngawi")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))