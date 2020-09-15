import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import os, os.path
import pickle

from nltk.corpus import stopwords
from wordcloud import WordCloud
from wordcloud import get_single_color_func

class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

class GroupedColorFunc(object):
    """Create a color function object which assigns DIFFERENT SHADES of
       specified colors to certain words based on the color to words mapping.

       Uses wordcloud.get_single_color_func

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

# check directory
path = 'image/'
cpath = os.path.exists(path)
if cpath == False:
    os.mkdir(path)

# load stopwords
with open('stopwords.pkl', 'rb') as f:
    list_stopwords = pickle.load(f)

# load cleaned raw string
data_clean = pd.read_pickle('data_clean.pkl')

# load object file list to use specific file
data_to = pd.read_pickle('object_file_list.pkl')

# load filtered word for coloring
with open('verb_set.pkl', 'rb') as f:
    verb_set = pickle.load(f)
with open('noun_set.pkl', 'rb') as f:
    noun_set = pickle.load(f)
with open('adj_set.pkl', 'rb') as f:
    adj_set = pickle.load(f)

# prepare the coloring process
color_to_words = {
    'red': list(verb_set),
    'green': list(noun_set),
    'blue': list(adj_set)
}

# default color for words that are not in color_to_word
default_color = 'grey'

# single color tone
# grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)

# multiple color tones
grouped_color_func = GroupedColorFunc(color_to_words, default_color)

# init wordcloud
wc = WordCloud(stopwords=list_stopwords, background_color='white', colormap='Dark2', width=1600, height=800)

# create wordcloud for every tourism object
for x in data_to.index:
    # combine all document into one
    wc_string = ''
    for c in data_to.columns:
        val = data_to.at[x, c]
        if val > 0:
            wc_string += ' ' + data_clean.text[c]

    # generate wordcloud
    wc.generate(wc_string)

    # recolor wordcloud
    wc.recolor(color_func=grouped_color_func)

    print ('wordcloud for ' + x + ' successfully created!')

    plt.figure( figsize=(20,10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(x)

    # export to png
    plt.savefig(path + x + '.png')
    plt.show()