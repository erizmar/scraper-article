import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import os, os.path
import pickle

from nltk.corpus import stopwords
from wordcloud import WordCloud

# load stopwords
with open('stopwords.pkl', 'rb') as f:
    list_stopwords = pickle.load(f)

# load object file list to use specific file
data_to = pd.read_pickle('object_file_list.pkl')

# init wordcloud
wc = WordCloud(stopwords=list_stopwords, background_color='white', colormap='Dark2', width=1600, height=800)

# list of filter
filter_list = ['verb', 'noun', 'adj', 'else']

# create wordcloud for every filter
for y in filter_list:
    # check directory
    path = 'image/filtered/' + y + '/'
    cpath = os.path.exists(path)
    if cpath == False:
        os.mkdir(path)

    # load filtered raw string
    data_filtered = pd.read_pickle('filter_' + y + '.pkl')

    for x in data_to.index:
        # combine all document into one
        wc_string = ''
        for c in data_to.columns:
            val = data_to.at[x, c]
            if val > 0:
                wc_string += ' ' + data_filtered.text[c]

        # generate wordcloud
        wc.generate(wc_string)

        print ('wordcloud for ' + x + ' ' + y + ' only successfully created!')

        plt.figure( figsize=(20,10))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(x + ' ' + y + ' only')

        # export to png
        plt.savefig(path + x + '.png')
        plt.show()