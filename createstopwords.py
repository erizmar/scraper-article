import mysql.connector
import pickle

from nltk.corpus import stopwords

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

# init stopwords
list_stopwords = set(stopwords.words('indonesian'))
list_stopwords.update(set(stopwords.words('english')))

for x in myresult:
    word = x[0].lower()
    list_stopwords.add(word)
    print (word)

# dump list stopwords
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(list_stopwords, f)

# add custom stopwords
# list_stopwords.update(['jl', 'rp', 'salah', 'source', 'image', 'credit', 'by', 'surabaya', 'wisata', 'kota', 'jawa', 'timur', 'lokasi', 'amp'])

# add custom stopwords from db
# with open('db_stopwords.pkl', 'rb') as f:
#     db_stopwords = pickle.load(f)
#     list_stopwords.update(db_stopwords)

