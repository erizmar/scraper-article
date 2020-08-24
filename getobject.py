import mysql.connector
import pickle

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  # password="yolomysql",
  database="pagedownload"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM tourism_object")

myresult = mycursor.fetchall()

list_objects = []

for x in myresult:
  list_objects.extend([x[0]])
  print (x[0])

with open('objectdb.pkl', 'wb') as f:
    pickle.dump(list_objects, f)