import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    # password="yolomysql",
    database="pagedownload"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT pubdate FROM links")
myresult = mycursor.fetchall()

pubdate = set()

for y in myresult:
    if y[0] == None:
        continue
    date = y[0]
    date = date[0:10]
    # pubdate.update([date])
    
    format = '%Y-%m-%d'
    if date != format:
        continue

    date = datetime.datetime.strptime(date, format)
    print (str(date))