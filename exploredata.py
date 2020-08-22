import pandas as pd
from nltk.corpus import stopwords

# init stopwords
list_stopword = set(stopwords.words('indonesian'))

# add custom stopwords
list_stopword.update(['jl', 'rp', 'salah', 'source', 'image', 'credit', 'by'])

data = pd.read_pickle('dtm.pkl')
data = data.transpose()
# data.head()

# top_dict = {}
# for c in data.columns:
#     top = data[c].sort_values(ascending=False).head(10)
#     top_dict[c]= list(zip(top.index, top.values))

# top_dict

data_clean = pd.read_pickle('data_clean.pkl')

from wordcloud import WordCloud

wc = WordCloud(stopwords=list_stopword, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)

import matplotlib.pyplot as plt

# plt.rcParams['figure.figsize'] = [16, 6]

# # Create subplots for each docs
# for index, x in enumerate(data.columns):
#     wc.generate(data_clean.text[x])
    
#     plt.subplot(3, 4, index+1)
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")

# Create bigplot
string = ''

for index, x in enumerate(data.columns):
    string += ' ' + data_clean.text[x]

wc.generate(string)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
wc.to_file("1.png")

# show wordcloud
plt.show()

# for value, top_words in top_dict.items():
#     print(value)
#     print(', '.join([word for word, count in top_words[0:14]]))
#     print('---')

# words = []
# for comedian in data.columns:
#     top = [word for (word, count) in top_dict[comedian]]
#     for t in top:
#         words.append(t)
        
# words