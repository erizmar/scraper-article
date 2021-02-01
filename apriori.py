import pandas as pd
import pickle

# load
data_dtm = pd.read_pickle('data_dtm_apr.pkl')

from mlxtend.frequent_patterns import apriori, association_rules
freq_items = apriori(data_dtm, min_support=0.2, use_colnames=True, verbose=1)
freq_items.to_pickle('freq_apr_new.pkl')
print(freq_items)

rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)
rules.to_pickle('rules_apr_new.pkl')
rules