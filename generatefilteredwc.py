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

# load document term matrix
data = pd.read_pickle('dtm.pkl')
data = data.transpose()

# load tourism object
tourism_object = ['aiola eatery', 'tugu pahlawan', 'pantai kenjeran', 'arca joko dolog', 'cakcuk cafe', 'delta plaza', 'taman bungkul']

# make tourism object document dictionary
to_dict = {}

# search the document containing tourism object
for x in tourism_object:
    # mark document appearance
    docf = {}

    # check if tourism object exist in document term matrix
    if x not in data.index:
        continue

    # search using dtm
    for c in data.columns:
        val = data.at[x, c]
        if val > 0:
            docf[c] = 1
        else:
            docf[c] = 0

    to_dict[x] = docf

# make dictionary into data frame
data_to = pd.DataFrame.from_dict(to_dict, orient='index')
data_to.to_pickle('object_file_list.pkl')
data_to

# wordcloud
wc = WordCloud(stopwords=list_stopwords, background_color='white', colormap='Dark2', width=1600, height=800)

wc_list = ['verb', 'noun', 'adj', 'else']
for y in wc_list:
    # check directory
    path = 'image/filtered/' + y + '/'
    cpath = os.path.exists(path)
    if cpath == False:
        os.mkdir(path)

    # load cleaned raw string
    data_clean = pd.read_pickle('filter_' + y + '.pkl')

    for x in tourism_object:
        # check if tourism object exist in document term matrix
        if x not in data.index:
            continue

        # filter docs
        wc_string = ''
        for c in data.columns:
            val = data_to.at[x, c]
            if val > 0:
                wc_string += ' ' + data_clean.text[c]

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