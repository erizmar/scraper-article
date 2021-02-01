import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

# load cleaned raw string
data_clean = pd.read_pickle('data_clean.pkl')

# load stopwords
with open('stopwords.pkl', 'rb') as f:
    list_stopwords = pickle.load(f)

# init tf-idf
tfidf = TfidfVectorizer(stop_words=list_stopwords)
data_tfidf = tfidf.fit_transform(data_clean.text)

data_dtm = pd.DataFrame(data_tfidf.toarray(), columns=tfidf.get_feature_names())
data_dtm.index = data_clean.index
data_dtm.to_pickle('data_dtm.pkl')

for c in data_dtm.columns:
    print ('processing index ' + str(c))
    data_dtm[c].mask(data_dtm[c] > 0, 1, inplace=True)


# for i in data_dtm.index:
#     print ('processing index ' + str(i))
#     for c in data_dtm.columns:
#         val = data_dtm.at[i, c]
#         if val > 0:
#             data_dtm.at[i, c] = 1
#         else:
#             data_dtm.at[i, c] = 0

# export
data_dtm.to_pickle('data_dtm_apr.pkl')