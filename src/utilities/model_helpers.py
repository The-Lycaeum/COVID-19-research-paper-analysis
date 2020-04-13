from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import re

## Pre-configured word embedding -- GLOVE (Stanford NLP)

def loadEmbeddings(filename):
    vocab2embd = {}

    with open(filename) as infile:
        for line in infile:
            row = line.strip().split(' ')
            word = row[0].lower()
            # print(word)
            if word not in vocab2embd:
                vec = np.asarray(row[1:], np.float32)
                if len(vec) == 100:
                    vocab2embd[word] = vec

    print('Embedding Loaded.')
        
    return vocab2embd