__author__ = 'Strahinja Ivanovic'

import unittest
import os
from src.data_loader import cleanData

class test_data_loader(unittest.TestCase):
    """ Test the data_loader.py methods"""

    def test_special_characters(self):
        """Test whether the cleanData()-method will remove all special characters"""
        cleanData(open("special_characters.txt", 'r'), "result1.txt")
        # should be empty
        self.assertFalse(os.stat('result1.txt').__contains__("!"))
        # remove the txt-file which was created by the test
        os.remove('result1.txt')

    def test_lower_letters(self):
        """Test whether the cleanData()-method will transform all uppercase-letter"""
        cleanData(open("lower_letters.txt", 'r'), "result2.txt")
        test_letters = open("result2.txt", "r")
        test_letters = str(test_letters.read())
        # should be no uppercase
        self.assertTrue(test_letters.islower())
        # remove the txt-file which was created by the test
        os.remove('result2.txt')

    def test_hashtags(self):
        """Test whether the cleanData()-method will remove all hashtags"""
        cleanData(open("hashtags.txt", 'r'), "result3.txt")
        test_letters = open("result3.txt", "r")
        test_letters = str(test_letters.read())
        # should be no hashtags
        self.assertEquals(test_letters.strip(), "hooray and up she rises")
        # remove the txt-file which was created by the test
        os.remove('result3.txt')

if __name__ == '__main__':
    unittest.main()



