import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import os, os.path

from nltk.corpus import stopwords
from wordcloud import WordCloud

# check directory
path = 'image/'
cpath = os.path.exists(path)
if cpath == False:
    os.mkdir(path)

# init stopwords
list_stopword = set(stopwords.words('indonesian'))

# add custom stopwords
list_stopword.update(['jl', 'rp', 'salah', 'source', 'image', 'credit', 'by', 'surabaya', 'wisata', 'kota', 'jawa', 'timur', 'lokasi'])

# load document term matrix
data = pd.read_pickle('dtm.pkl')
data = data.transpose()

# load cleaned raw string
data_clean = pd.read_pickle('data_clean.pkl')

# load tourism object
tourism_object = ['aiola eatery', 'tugu pahlawan', 'pantai kenjeran', 'surabaya']

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
    
    # # search using regex
    # count = 1
    # while count < 6:
    #     find = '.*' + x + '*.'
    #     find_string = re.search(find, data_clean.text[count])
    #     if find_string:
    #         print (x + ' match found in doc ' + str(count))
    #         docf[count] = 1
    #     else:
    #         print ('no match for ' + x)
    #         docf[count] = 0
    #     count += 1

    to_dict[x] = docf

# make dictionary into data frame
data_to = pd.DataFrame.from_dict(to_dict, orient='index')
data_to

# wordcloud
wc = WordCloud(stopwords=list_stopword, background_color='white', colormap='Dark2',
               max_font_size=150, random_state=42)

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

    # export to png
    wc.to_file(path + x + '.png')
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(x)
    plt.show()