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
    word = x[0].lower()
    list_stopwords.add(word)
    print (word)

with open('db_stopwords.pkl', 'wb') as f:
    pickle.dump(list_stopwords, f)