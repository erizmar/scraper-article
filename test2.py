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

for x in myresult:
    alias = x[1]
    if alias is not None:
        alias = alias.split(sep=',')
        alias_dict = {}
        for y in alias:
            index_val = alias.index(y)
            alias_dict[index_val] = y
        object_dict[x] = alias_dict
    else:
        object_dict[x] = None
         
    print (x[0])

with open('db_object.pkl', 'wb') as f:
    pickle.dump(object_dict, f)