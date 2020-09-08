import pandas as pd
import pickle

data_tagged = pd.read_pickle('data_tagged.pkl')

verb_dict = {}
noun_dict = {}
adj_dict = {}
else_dict = {}

for x in data_tagged.index:
    text = data_tagged.text[x].split()
    verb_string = ''
    noun_string = ''
    adj_string = ''
    else_string = ''

    for y in text:
        if y == '<VERB>':
            index_val = text.index(y)
            text[index_val] = 'DONE'
            index_val = index_val-1
            verb_string += text[index_val] + ' '

        elif y == '<NOUN>':
            index_val = text.index(y)
            text[index_val] = 'DONE'
            index_val = index_val-1
            noun_string += text[index_val] + ' '

        elif y == '<ADJ>':
            index_val = text.index(y)
            text[index_val] = 'DONE'
            index_val = index_val-1
            adj_string += text[index_val] + ' '

        elif y.startswith('<'):
            index_val = text.index(y)
            text[index_val] = 'DONE'
            index_val = index_val-1
            else_string += text[index_val] + ' '

    print ('doc ' + str(x) + ' filtered')
    verb_dict[x] = verb_string
    noun_dict[x] = noun_string
    adj_dict[x] = adj_string
    else_dict[x] = else_string
    
data_filter_verb = pd.DataFrame.from_dict(verb_dict, orient='index')
data_filter_verb.columns = ['text']
data_filter_verb.to_pickle('filter_verb.pkl')

data_filter_noun = pd.DataFrame.from_dict(noun_dict, orient='index')
data_filter_noun.columns = ['text']
data_filter_noun.to_pickle('filter_noun.pkl')

data_filter_adj = pd.DataFrame.from_dict(adj_dict, orient='index')
data_filter_adj.columns = ['text']
data_filter_adj.to_pickle('filter_adj.pkl')

data_filter_else = pd.DataFrame.from_dict(else_dict, orient='index')
data_filter_else.columns = ['text']
data_filter_else.to_pickle('filter_else.pkl')

verb_list = []
for x in data_filter_verb.index:
    text = data_filter_verb.text[x].split()
    verb_list.extend(text)
verb_set = set(verb_list)
with open('verb_set.pkl', 'wb') as f:
    pickle.dump(verb_set, f)

noun_list = []
for x in data_filter_noun.index:
    text = data_filter_noun.text[x].split()
    noun_list.extend(text)
noun_set = set(noun_list)
with open('noun_set.pkl', 'wb') as f:
    pickle.dump(noun_set, f)

adj_list = []
for x in data_filter_adj.index:
    text = data_filter_adj.text[x].split()
    adj_list.extend(text)
adj_set = set(adj_list)
with open('adj_set.pkl', 'wb') as f:
    pickle.dump(adj_set, f)