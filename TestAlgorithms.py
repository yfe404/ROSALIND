__author__ = 'yafeunteun'


import unittest
from frequentWordProblem import fasterMostFrequentsKMers

class TestAlgorithms(unittest.TestCase):

    def test_frequentWordProblem(self):
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        result = ["CATG", "GCAT"]

        self.assertListEqual(result, fasterMostFrequentsKMers(text, 4))





if __name__ == '__main__':
    unittest.main()


