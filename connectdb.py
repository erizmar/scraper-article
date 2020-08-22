import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pagedownload"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM list")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)