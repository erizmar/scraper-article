import pandas as pd
import re
import string
import os, os.path
import pickle

# doc count
path = 'download/text/'
total_doc = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

# counter
count = 1

# for storing all document
data_dict = {}

# load stopwords
with open('stopwords.pkl', 'rb') as f:
    list_stopwords = pickle.load(f)

# load tourism object
with open('list_to.pkl', 'rb') as f:
    list_to = pickle.load(f)

# adding all docs to dictionary
while count <= total_doc:
    print ('opening doc ' + str(count))
    with open (path+str(count)+"-plaintext.txt", "r", errors="ignore") as myfile:
        text = myfile.read()

    # cleaning the file
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\d', '', text)
    # text = re.sub('[‘’“”…ƒâãšÿž€¢¦œ²³º¼¾]', '', text)
    text = re.sub('[^a-zA-Z ]+', '', text)
    text = re.sub('\n', '', text)

    for y in list_to:
        ysub = re.sub(' ', '_', y)
        text = re.sub(y, ysub, text)
    
    stext = text.split()
    text = ''
    for x in stext:
        if len(x) >= 25:
            stext.remove(x)
        else:
            text += x + ' '
    
    data_dict[count] = text

    count += 1

# changing dictionary to dataframe
data_clean = pd.DataFrame.from_dict(data_dict, orient='index')
data_clean.columns = ['text']
data_clean.to_pickle('data_clean.pkl')
data_clean