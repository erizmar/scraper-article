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

for i in data_dtm.index:
    print ('processing index ' + str(i))
    for c in data_dtm.columns:
        val = data_dtm.at[i, c]
        if val > 0:
            data_dtm.at[i, c] = 1
        else:
            data_dtm.at[i, c] = 0

# export
data_dtm.to_pickle('data_dtm_apr.pkl')

from mlxtend.frequent_patterns import apriori, association_rules
freq_items = apriori(data_dtm, min_support=0.2, use_colnames=True, verbose=1)
freq_items.to_pickle('freq_apr.pkl')
freq_items.head(7)

rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)
rules.to_pickle('rules_apr.pkl')
rules.head(7)