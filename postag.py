import pandas as pd
import pickle

from flair.data import Sentence
from flair.models import SequenceTagger
from flair.models import TextClassifier

# load cleaned raw string
data_clean = pd.read_pickle('data_clean.pkl')

# use trained model
tag_pos = SequenceTagger.load('resources/best-model.pt')

# for storing pos tagged string
tag_dict = {}

# for every doc
for x in data_clean.index:
    sentence = Sentence(data_clean.text[x])
    tag_pos.predict(sentence)
    tag_dict[x] = sentence.to_tagged_string()
    print ('doc ' + str(x) + ' tagged')

data_tagged = pd.DataFrame.from_dict(tag_dict, orient='index')
data_tagged.columns = ['text']

# dump data
data_tagged.to_pickle('data_tagged.pkl')
data_tagged