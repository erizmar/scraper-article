import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import os, os.path
import pickle
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    # password="yolomysql",
    database="pagedownload"
)

# load
data = pd.read_pickle('object_file_list.pkl')

# make tourism object document dictionary
to_dict = {}

# search the document containing tourism object
for x in data.index:
    a_dict = {}

    # search using dtm
    for c in data.columns:
        val = data.at[x, c]
        if val == 1:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT pubdate FROM links WHERE id = " + str(c))
            myresult = mycursor.fetchall()

            pubdate = set()

            for y in myresult:
                if y[0] == None:
                    continue
                date = y[0]
                date = date[0:7]
                
                format = '%Y-%m'
                date = datetime.datetime.strptime(date, format)
                # print (str(c) + ': ' + str(date))

                if date in a_dict:
                    a_dict[date] += 1
                else:
                    a_dict[date] = 1
                
                a_dict
        else:
            continue

    to_dict[x] = a_dict
    to_dict

# make dictionary into data frame
data_tt = pd.DataFrame.from_dict(to_dict, orient='index')
# data_tt.columns = ['id']
data_tt.to_pickle('object_id_list.pkl')
data_tt = data_tt.transpose()
# data_tt.index('Month')
data_tt.plot(grid=True)
