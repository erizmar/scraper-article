import re
import pandas as pd

data_clean = pd.read_pickle('data_clean.pkl')
data_tagged = pd.read_pickle('tagged.pkl')

### Extracting POS tags ###
## in every sentence by index ##
for i in data_tagged.index:
    ## for every words ith sentence ##
    for j in data_clean.text[i].split():
        ## replace that word from ith sentence in f_pos ##
        data_tagged.text[i] = str(data_tagged.text[i]).replace(j,"",1)

    ## Removing < > symbols ##
    for j in  ['<','>']:
        data_tagged.text[i] = str(data_tagged.text[i]).replace(j,"")

        ## removing redundant spaces ##
        # data_tagged.text[i] = re.sub(' +', ' ', str(data_tagged.text[i]))
        # data_tagged.text[i] = str(data_tagged.text[i]).lstrip()

# data_tagged.to_pickle('tag_only.pkl')
data_tagged