__author__ = 'yafeunteun'

"""
Frequent Words Problem

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).
"""

import numpy as np



"""
Returns the number of times that a k-mer Pattern appears as a substring of Text
"""
def count(text, pattern):
    count = 0

    return text.count(pattern)


"""
Return: All most frequent k-mers in Text (in any order).
"""
def mostFrequentsKMers(text, k):

    textLen = len(text)
    indices = np.zeros(textLen)
    mostFrequents = set()
    maxFrequency = 0

    for i in range(textLen - k):
        indices[i] = count(text, text[i:i+k])

    maxFrequency = indices.max()

    for i in range(textLen-k):
        if indices[i] == maxFrequency:
            mostFrequents.add(text[i:i+k])

    return mostFrequents


def main():

    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4

    for pattern in mostFrequentsKMers(text, k):
        print(pattern)



if __name__ == '__main__':
    main()

