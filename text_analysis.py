import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import os
import json
from collections import Counter
import operator

directory = 'lyrics/unique/processed/'
files = os.listdir(directory)
#files = ['lyrics/unique/processed/7MinutesInHeavenAtavanHalen.txt']
lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
lemmas = []
verb_pos = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
verbs = []

def lemmatize_song(text):
    tokens = nltk.word_tokenize(text)
    pos_tokens = nltk.pos_tag(tokens)

    for token, pos in pos_tokens:
        if pos in verb_pos:
            verbs.append(token)

for file in files:
    with open(directory + file, 'r') as f:
        text = f.read()
        lemmatize_song(text)
        f.close()

for token in verbs:
    lemma = lmtzr.lemmatize(token, wn.VERB)
    lemmas.append(lemma)

stop_words = set(stopwords.words('english'))
lemmas = [w for w in lemmas if not w in stop_words]

freq = Counter(lemmas)

freq = dict(freq)

# thx https://stackoverflow.com/a/613218
sorted_frq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_frq)


#lemma_set = set(lemmas)
#print(lemma_set)


#ings = []
# for token in tokens:
#     if token.endswith('ing'):
#         ings.append(token)
#
# print(ings)

#sentences = nltk.sent_tokenize(text)
#tagged_tokens = nltk.pos_tag(tokens)

#lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
#lemma=lmtzr.lemmatize(tokens[4], 'v')

#print(tokens)
#print(sentences)
#print(tagged_tokens)
#print(lemma)
