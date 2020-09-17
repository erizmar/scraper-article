import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer

# load cleaned raw string
data_clean = pd.read_pickle('data_clean.pkl')

# load stopwords
with open('stopwords.pkl', 'rb') as f:
    list_stopwords = pickle.load(f)

# init count vectorizer using custom stopwords and bigrams
cv = CountVectorizer(stop_words=list_stopwords, ngram_range=(1, 3))

data_cv = cv.fit_transform(data_clean.text)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index

# dump data
data_dtm.to_pickle('data_dtm.pkl')
data_dtm

# # TFIDF
# from sklearn.feature_extraction.text import TfidfVectorizer

# tfidf = TfidfVectorizer(stop_words=list_stopwords, ngram_range=(1, 2))

# data_dtm = tfidf.fit_transform(data_clean.text)
# data_dtm = pd.DataFrame(data_dtm.toarray(), columns=tfidf.get_feature_names())
# data_dtm.index = data_clean.index

# data_dtm.to_pickle("dtm.pkl")
# data_dtm