#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Data management unit for the tweetanalyzer. """

__author__ = 'Strahinja Ivanovic'

# Import needed utilities

import re
from nltk.corpus import stopwords
import HTMLParser

html_parser = HTMLParser.HTMLParser()
APPOSTROPHES = {"'s":"is", "'re":"are", "'m":"am", "'t":"not", "'ll":"will", "ill":"I will", "im":"I am",
                "wanna":"want to", "gonna": "going to"}

def cleanData(rawTweets, outputfile):
 """
 Cleans the given Data according to certain text mining methods and prints the cleaned output in a textfile
 :param rawTweets: Input source which has to be cleaned
 :param outputfile: Name the ouput file should have
 :return:
 """
 NewFile = open(outputfile, 'w')
 for eachline in rawTweets:
  # decode to UTF-8
  cleanedTweets = eachline.decode("utf8").encode('ascii', 'ignore')
  # remove html tags
  cleanedTweets = html_parser.unescape(cleanedTweets)
  # lower all letters for standardization
  cleanedTweets = cleanedTweets.lower()
  # remove apostrophes and standardize data
  cleanedTweets = [APPOSTROPHES[word] if word in APPOSTROPHES else word for word in cleanedTweets.split()]
  cleanedTweets = " ".join(cleanedTweets)
  # remove stopwords
  #cleanedTweets = ' '.join([word for word in cleanedTweets.split() if word not in stopwords.words("english")])
  # remove links
  cleanedTweets = re.sub(r'http\S+', '', cleanedTweets)
  # remove hasthags
  cleanedTweets = re.sub(r'#\w+ ?', '', cleanedTweets)
  # remove remaining special characters
  cleanedTweets = re.sub('[^A-Za-z0-9 ]+','',cleanedTweets)
  # print the output in a new File
  NewFile.write('%s \n' % cleanedTweets)



