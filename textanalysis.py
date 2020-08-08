import spacy
from collections import Counter
from spacy.lang.en import English
nlp = English()
text = """Most of the outlay will be at home. No surprise there, either. While Samsung has expanded overseas, South Korea is still host to most of its factories and research engineers. """
doc = nlp(text)
words = [token.text for token in doc]
print (words)