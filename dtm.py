import pandas as pd
import nltk.corpus
import re
import string
import os, os.path
import pickle

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# doc count
path = 'download/text/'
total_doc = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

# counter
count = 1

# make dictionary
data_dict = {}

# init stopwords
list_stopwords = set(stopwords.words('indonesian'))

# add custom stopwords
list_stopwords.update(['jl', 'rp', 'salah', 'source', 'image', 'credit', 'by', 'surabaya', 'wisata', 'kota', 'jawa', 'timur', 'lokasi', 'amp'])
# with open('stopwordsdb.pkl', 'rb') as f:
#     db_stopwords = pickle.load(f)
#     list_stopwords.update(db_stopwords)

with open('stopwords.pkl', 'wb') as f:
    pickle.dump(list_stopwords, f)

# adding all docs to dictionary
while count <= total_doc:
    print ('opening doc ' + str(count))
    with open (path+str(count)+"-plaintext.txt", "r", errors="ignore") as myfile:
        text = myfile.read()

    # cleaning the file
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    
    data_dict[count] = text

    count += 1

# changing dictionary to dataframe
data_clean = pd.DataFrame.from_dict(data_dict, orient='index')
data_clean.columns = ['text']

# init count vectorizer using custom stopwords and bigrams
cv = CountVectorizer(stop_words=list_stopwords, ngram_range=(1, 2))

data_cv = cv.fit_transform(data_clean.text)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index

# dump to csv
# data_dtm.to_csv("dtm.csv")

# dump to pickle
data_dtm.to_pickle("dtm.pkl")
data_clean.to_pickle("data_clean.pkl")
data_dtm

print ("document term matrix successfully created!")

# # init tf-idf using custom stopwords and bigrams
# tfidf = TfidfVectorizer(stop_words=list_stopwords, ngram_range=(1, 2))

# data_dtm = tfidf.fit_transform(data_clean.text)
# data_dtm = pd.DataFrame(data_dtm.toarray(), columns=tfidf.get_feature_names())
# data_dtm.index = data_clean.index

# data_dtm.to_pickle("dtm.pkl")
# data_dtm