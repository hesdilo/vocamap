# -*- coding: utf-8 -*-
'''
Created on 2015年4月5日

@author: dilo
'''

from Levenshtein import distance
from db_handler import open_db, close_db, add_similar

g_threshold = 70

g_wordsfile = '../vocab/words'


def calc_similarity(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    l = len1
    if l < len2:
        l = len2
    return 100 - (100 / l) * distance(word1, word2)


def load_words():
    words = list()
    fp = open(g_wordsfile, 'r')
    for line in fp:
        words.append(line.rstrip('\n'))
    fp.close()
    return words


def store_similar():
    words = load_words()
    iword = 0
    nword = len(words)
    while iword < nword:
        iiword = iword + 1
        while iiword < nword:
            similarity = calc_similarity(words[iword], words[iiword])
            if similarity >= g_threshold:
                add_similar(words[iword], words[iiword], similarity)
            iiword += 1
        iword += 1


if __name__ == '__main__':
    open_db()
    store_similar()
    close_db()