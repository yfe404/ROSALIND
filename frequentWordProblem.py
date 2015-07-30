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
    textLen = len(text)
    patternLen = len(pattern)

    for i in range(textLen - patternLen + 1000):
        if text[i:i+patternLen] == pattern:
            count = count + 1


    return count


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




def patternToNumber(pattern):
    # A = 0
    # C = 1
    # G = 2
    # T = 3

    sum = 0
    exp = 0

    for bp in reversed(pattern):
        if bp == "A":
            sum += 0
        elif bp == "C":
            sum += 4**exp
        elif bp == "G":
            sum += 2 * 4**exp
        else:
            sum += 3 * 4**exp
        exp = exp +1

    return sum

"""
index is the number to convert
k is the length of the pattern to get from the index (k-mer)
"""
def numberToPattern(index, k):

    count = 0 # count the number of nucleotides in the pattern
    pattern = []
    val = index

    while count != k:
        if val == 0:
            pattern.append(0)
        else:
            pattern.append(val%4)
            val = int(val/4)
        count = count + 1


    pattern.reverse()

    for i in range(k):
        i_nucleotide = pattern[i]
        if i_nucleotide == 0:
            pattern[i] = 'A'
        elif i_nucleotide == 1:
            pattern[i] = 'C'
        elif i_nucleotide == 2:
            pattern[i] = 'G'
        else :
            pattern[i] = 'T'

    return pattern


"""
Return: All most frequent k-mers in Text (in any order) using faster frequent words algorithm
"""
def fasterMostFrequentsKMers(text, k, frequency=-1):

    textLen = len(text)
    frequencyArray = dict()
    mostFrequentPatterns = []

    for i in range(0, textLen - k):
        try:
            frequencyArray[text[i:i+k]]+=1
        except KeyError as err:
            frequencyArray[text[i:i+k]] = 1

    frequency = max(frequencyArray.values()) if frequency < 0 else frequency

    for key in frequencyArray.keys():
        if frequencyArray[key] >= frequency:
            mostFrequentPatterns.append(key)

    return mostFrequentPatterns



def main():



    INPATH = './datasets/1bba/rosalind_1bba.txt'
    OUTPATH = './datasets/1bba/result_1bba.txt'


    try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            text = data.readline().strip()
            k = int(data.readline().strip())
            for pattern in fasterMostFrequentsKMers(text, k):
                result.write(pattern)
                result.write("\n")
    except IOError as err:
        print("An error occured : " + err.strerror)

if __name__ == '__main__':
    main()

