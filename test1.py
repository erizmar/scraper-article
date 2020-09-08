import pandas as pd

data = pd.read_pickle('dtm.pkl')
data = data.transpose()

data_clean = pd.read_pickle('data_clean.pkl')

tourism_object = {'aiola eatery': None, 'pantai ria kenjeran': {0: 'pantai kenjeran', 1: 'kenjeran'}, 'plaza surabaya': {0: 'plasa surabaya', 1: 'delta plaza'}}

# make tourism object document dictionary
to_dict = {}

for x in tourism_object:
    # mark document appearance
    docf = {}

    print ('Object: '+x)
    alias = tourism_object[x]

    if alias is None:
        # check if tourism object exist in document term matrix
        if x not in data.index:
            continue

        # search using dtm
        for c in data.columns:
            val = data.at[x, c]
            if val > 0:
                docf[c] = 1
            else:
                docf[c] = 0

        to_dict[x] = docf
    else:
        alias['obj'] = x
        for y in alias:
            a = alias[y]
            print ('Object + Alias: '+a)
            if a not in data.index:
                continue

            # search using dtm
            for c in data.columns:
                if c in docf:
                    a_val = docf[c]
                    val = data.at[a, c]

                    if a_val == 1 or val > 0:
                        docf[c] = 1
                    else:
                        docf[c] = 0
                else:
                    val = data.at[a, c]
                    if val > 0:
                        docf[c] = 1
                    else:
                        docf[c] = 0

        to_dict[x] = docf

# make dictionary into data frame
data_to = pd.DataFrame.from_dict(to_dict, orient='index')
# data_to.to_pickle('object_file_list.pkl')
data_to