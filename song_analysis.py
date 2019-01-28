import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import os
import json
from collections import Counter
import operator
import csv

directory = 'lyrics/unique/processed/'
files = os.listdir(directory)
#files = ['ChicagoIsSoTwoYearsAgo.txt']
lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
verb_pos = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

violent_words = ['kill',
'die',
'drive',
'leave',
'end',
'stop',
'throw',
'cut',
'burn',
'hurt',
'scream',
'swear',
'deserve',
'bury',
'break',
'pay',
'choke',
'sharpen', 'douse', 'slit', 'overdose', 'demote', 'suffocate', 'force', 'terrify', 'drown', 'dead', 'hunt', 'sedate', 'mummify', 'blackmail', 'hate']

def find_verbs(text, song, file):
    lemmas = []
    verbs = []
    tokens = nltk.word_tokenize(text)
    pos_tokens = nltk.pos_tag(tokens)
    words_in_song = []

    for token, pos in pos_tokens:
        if pos in verb_pos:
            verbs.append(token)

    for token in verbs:
        lemma = lmtzr.lemmatize(token, wn.VERB)
        lemmas.append(lemma)

    for l in lemmas:
        if l in violent_words:
            words_in_song.append(l)

    words_in_song = set(words_in_song)

    if len(words_in_song) > 1:
        row = [song, len(song) -4, len(words_in_song)]
        for w in words_in_song:
            row.append(w)
        return row


with open('edited_songs_list.csv', 'a') as s:
    for file in files:
        with open(directory + file, 'r') as f:
            text = f.read()
            row = find_verbs(text, file, s)
            if row:
                writer = csv.writer(s)
                writer.writerow(row)
            f.close()
    s.close()
