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

mycursor.execute("SELECT name, alias FROM tourism_object")

myresult = mycursor.fetchall()

object_dict = {}

for row in myresult:
    name = row[0].lower()
    alias = row[1]
    if alias is not None:
        alias = alias.lower().split(sep=',')
        alias_dict = {}
        for y in alias:
            index_val = alias.index(y)
            alias_dict[index_val] = y
        object_dict[name] = alias_dict
    else:
        object_dict[name] = None

with open('db_object.pkl', 'wb') as f:
    pickle.dump(object_dict, f)