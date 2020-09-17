import pickle

from nltk.corpus import stopwords

# init stopwords
list_stopwords = set(stopwords.words('indonesian'))

# add custom stopwords
list_stopwords.update(['jl', 'rp', 'salah', 'source', 'image', 'credit', 'by', 'surabaya', 'wisata', 'kota', 'jawa', 'timur', 'lokasi', 'amp'])

# add custom stopwords from db
# with open('db_stopwords.pkl', 'rb') as f:
#     db_stopwords = pickle.load(f)
#     list_stopwords.update(db_stopwords)

# dump list stopwords
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(list_stopwords, f)