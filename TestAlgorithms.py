__author__ = 'yafeunteun'


import unittest
from frequentWordProblem import fasterMostFrequentsKMers
from reverseComplementProblem import reverseComplement

class TestAlgorithms(unittest.TestCase):

    def test_frequentWordProblem(self):
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        result = ["CATG", "GCAT"]

        self.assertListEqual(sorted(result), sorted(fasterMostFrequentsKMers(text, 4)))

    def test_reverseComplementProblem(self):
        text = "AAAACCCGGT"
        self.assertEqual("ACCGGGTTTT", "".join(reverseComplement(text)))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgorithms)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()


