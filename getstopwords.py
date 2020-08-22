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

mycursor.execute("SELECT word FROM stopwords")

myresult = mycursor.fetchall()

list_stopwords = set()

for x in myresult:
  list_stopwords.update([x[0]])
  print (x[0])

with open('stopwordsdb.pkl', 'wb') as f:
    pickle.dump(list_stopwords, f)