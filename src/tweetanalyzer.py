#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main module for the script. Run this python-file to execute the program. """

__author__ = 'Strahinja Ivanovic'

import os
from data_loader import cleanData
from calculator import getNgram

print("Loading and cleaning the Data...")
cleanData(open("tweets.txt", "r"),"cleaneddata.txt")
print("Data cleaned.")
print("Calculating the n-grams")

tmpFile = open('cleaneddata.txt', 'r')
tmpFile = tmpFile.read()

# calculate the 500 most common unigrams
getNgram(tmpFile ,"unigrams.txt",1,500)
print("unigrams.txt created.")
# calculate the 100 most common bigrams
getNgram(tmpFile ,"bigrams.txt",2,100)
print("bigrams.txt created.")
# calculate the 100 most common trigrams
getNgram(tmpFile,"trigrams.txt",3,100)
print("trigrams.txt created.")
# remove temporary file
os.remove('cleaneddata.txt')