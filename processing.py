#coding:utf-8

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import *

ps = PorterStemmer()

def implStopwordStemmer(init_word):
    tokenized_word = word_tokenize(init_word)                  #tokenize

    stop_wordlist = set(stopwords.words("english"))            #remove stopwords
    remov_stopword = [w for w in tokenized_word if w not in stop_wordlist]

    stemmed_words = []                                         #stemmer
    for w in remov_stopword:
        stemmed_words.append(ps.stem(w))

    return ' '.join(stemmed_words)





