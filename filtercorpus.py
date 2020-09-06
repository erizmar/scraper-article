import pandas as pd

data_tagged = pd.read_pickle('tagged.pkl')

filtered_dict = {}

for x in data_tagged.index:
    text = data_tagged.text[x].split()
    giant_string = ''

    for y in text:
        # take verb word
        if y == '<NOUN>':
            index_val = text.index(y)
            text[index_val] = 'DONE'
            index_val = index_val-1
            giant_string += text[index_val] + ' '
        
    print ('doc ' + str(x) + ' filtered')
    filtered_dict[x] = giant_string
    
data_wordonly = pd.DataFrame.from_dict(filtered_dict, orient='index')
data_wordonly.columns = ['text']

data_wordonly.to_pickle('filtered.pkl')
data_wordonly