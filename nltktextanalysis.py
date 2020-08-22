import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import MWETokenizer
# from sklearn.feature_extraction.text import CountVectorizer

# doc count
count = 1
total_doc = 5

# make empty list
word_doc = []

# list of stopwords
list_stopword = set(stopwords.words('indonesian'))

# add custom multi-words token
tokenizer = MWETokenizer([('kota', 'surabaya'), ('image', 'credit', 'by')])

# add custom stopwords
list_stopword.update(['jl', 'rp', 'salah', 'source'])

while count < total_doc+1:
    with open ("download/text/"+str(count)+"-plaintext.txt", "r") as myfile:
        text = myfile.read()

    text = text.translate(str.maketrans("", "", string.punctuation))
    
    tokens = tokenizer.tokenize(text.lower().split())

    removed = []
    for t in tokens:
        if t not in list_stopword:
            removed.append(t)

    word_doc.extend(removed)

    fdist = FreqDist(removed)

    common_words = fdist.most_common(10)
    print ("Doc "+str(count))
    print (common_words)

    # cv = CountVectorizer(stop_words='english')
    # data_cv = cv.fit_transform(data_clean.transcript)
    # data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
    # data_dtm.index = data_clean.index
    # data_dtm

    count += 1

doc_word_freq = FreqDist(word_doc)
doc_common_words = doc_word_freq.most_common(10)

print ("All Doc")
print (doc_common_words)