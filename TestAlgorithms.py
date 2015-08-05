__author__ = 'yafeunteun'


import unittest
from frequentWordProblem import fasterMostFrequentsKMers
from reverseComplementProblem import reverseComplement
from patternMatchingProblem import patternMatching

class TestAlgorithms(unittest.TestCase):

    def test_frequentWordProblem(self):
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        result = ["CATG", "GCAT"]

        self.assertListEqual(sorted(result), sorted(fasterMostFrequentsKMers(text, 4)))

    def test_reverseComplementProblem(self):
        text = "AAAACCCGGT"
        self.assertEqual("ACCGGGTTTT", "".join(reverseComplement(text)))

    def test_patternMatchingProblem(self):
        pattern = "ATAT"
        text = "GATATATGCATATACTT"

        self.assertListEqual(sorted(["1", "3", "9"]), sorted(patternMatching(pattern, text) ))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgorithms)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()


