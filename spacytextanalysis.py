import spacy
from collections import Counter

count = 1
total_doc = 5

# make empty list
word_doc = []

# using multi-language
nlp = spacy.load("xx_ent_wiki_sm")

# open stripped html
while count < total_doc+1:
    with open ("download/"+str(count)+"-plaintext.txt", "r") as myfile:
        text = myfile.read()

    doc = nlp(text)
    # words = [token.text for token in doc]
    words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

    # count words this doc
    word_freq = Counter(words)

    # add this doc list to all doc list
    word_doc.extend(words)

    common_words = word_freq.most_common(5)
    print ("Doc "+str(count))
    print (common_words)

    count += 1

doc_word_freq = Counter(word_doc)
doc_common_words = doc_word_freq.most_common(5)

print ("All Doc")
print (doc_common_words)