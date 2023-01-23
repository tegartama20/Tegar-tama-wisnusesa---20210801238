import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="bahasa_pemprograman"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("wisnu", "Tangerang"),
  ("Nadia", "Surabaya"),
  ("Bella", "Bandung"),
  ("Nabila", "Jakarta")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))