#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Calculating unit for the tweetanalyzer. """

__author__ = 'Strahinja Ivanovic'

# Import needed utilities

import nltk
from nltk.util import ngrams
from collections import Counter

def getNgram(data,name,n,amount):
    """
    Analyzes a given source, counts the number of n-grams and prints the results in a textfile.
    :param data: The source which should be analyzed
    :param name: Name the output should have (textfile)
    :param n: logical parameter for the size of the n-gram (1 = unigram, 2 = bigram ...)
    :param amount: parameter for the most common n-grams. If this parameter is 100, the script
    will return the 100 most common n-grams
    :return: Textfile with the results
    """

    token = nltk.word_tokenize(str(data))
    # tokenize the data
    neededNgrams = ngrams(token,n)
    targetFile = open(name, "w")
    # create target file
    for letter, count in Counter(neededNgrams).most_common(amount):
        # print the most common n-grams into the target file
        targetFile.write('%s:%7d \n' % (letter, count))

