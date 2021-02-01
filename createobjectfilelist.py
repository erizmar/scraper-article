import pandas as pd
import pickle
import re

# load document term matrix
data_dtm = pd.read_pickle('data_dtm.pkl')
# transpose for word index
data_dtm = data_dtm.transpose()

# load cleaned raw string
data_clean = pd.read_pickle('data_clean.pkl')

# load tourism object
# with open('db_object.pkl', 'rb') as f:
#     tourism_object = pickle.load(f)
tourism_object = {'aiola eatery': None, 'tugu pahlawan': None, 'pantai ria kenjeran': {0: 'pantai kenjeran'}, 'plaza surabaya': {0: 'plasa surabaya', 1: 'delta plaza'}, 'taman bungkul': None}

# make tourism object document dictionary
to_dict = {}

for x in tourism_object:
    # substitute space
    x = re.sub(' ', '_', x)

    # for storing document appearance
    docf = {}

    # treat value of every key as alias
    alias = tourism_object[x]

    # for empty aliases
    if alias is None:
        # check if tourism object exist in document term matrix
        if x not in data_dtm.index:
            continue

        # tag document appearance
        for c in data_dtm.columns:
            val = data_dtm.at[x, c]
            if val > 0:
                docf[c] = 1
            else:
                docf[c] = 0

        to_dict[x] = docf

    else:
        # add name as an alias
        alias['obj'] = x

        # for every alias
        for y in alias:
            a = alias[y]

            # check if tourism object exist in document term matrix
            if a not in data_dtm.index:
                continue

            # tag document appearance
            for c in data_dtm.columns:
                # combine all appearance
                if c in docf:
                    # check previous iteration result and combine with current search on dtm 
                    a_val = docf[c]
                    val = data_dtm.at[a, c]

                    if a_val == 1 or val > 0:
                        docf[c] = 1
                    else:
                        docf[c] = 0
                else:
                    # first iteration checking only dtm
                    val = data_dtm.at[a, c]
                    if val > 0:
                        docf[c] = 1
                    else:
                        docf[c] = 0

        to_dict[x] = docf

# make dictionary into data frame
data_to = pd.DataFrame.from_dict(to_dict, orient='index')

# dump data
data_to.to_pickle('object_file_list.pkl')
data_to