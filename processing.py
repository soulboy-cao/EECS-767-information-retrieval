#coding:utf-8

import re
import os
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


def processing(origin_path, targetpath):
    origin_files = [file for file in os.listdir(origin_path) if file.endswith(".htm") or file.endswith(".html")]
    # print(origin_files)
    for file_item in origin_files:
        file = open(origin_path + str(file_item), mode='r', encoding='UTF-8')
        data = file.read()
        file.close()
        # extract text from html
        text = filter_tags(data)
        # stemming
        result = implStopwordStemmer(text)
        output = open(targetpath + str(file_item) + '.txt', mode='w+', encoding='UTF-8')
        output.write(result)
        output.close()


def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ','lt':'<','60':'<', 'gt':'>','62':'>','amp':'&','38':'&','quot':'"','34':'"'}
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    word=re_charEntity.search(htmlstr)
    while word:
        key=word.group('name')
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            word = re_charEntity.search(htmlstr)
        except KeyError:
            htmlstr = re_charEntity.sub('',htmlstr,1)
            word = re_charEntity.search(htmlstr)
    return htmlstr


def filter_tags(htmlstr):
    # Filter models
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I)               #for CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)   #style
    re_comment = re.compile('<!--[^>]*-->')                                #comments
    re_h = re.compile(r'<[^>]+>')                                          #tags

    s = re_cdata.sub('',htmlstr)                                          #remove CDATA
    s = re_script.sub('',s)                                               #remove SCRIPT
    s = re_style.sub('',s)                                                #remove style
    s = re_h.sub('',s)                                                    #remove tags
    s = re_comment.sub('',s)                                              #remove comments
    s = replaceCharEntity(s)                                              #remove special cha

    s = ' '.join(s.split())                                               #remove spaces
    s = s.lower()
    return s





