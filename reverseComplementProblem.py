#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      feunteuny
#
# Created:     27/07/2015
# Copyright:   (c) feunteuny 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


"""
Find the reverse complement of a DNA string.

Works either with dnaString as a list or as a string
"""

def reverseComplement(dnaString):

    if type(dnaString) == str:
        dnaString = list(dnaString)

    for i in range(len(dnaString)):
        if dnaString[i] == 'A':
            dnaString[i] = 'T'
        elif dnaString[i] == 'T':
            dnaString[i] = 'A'
        elif dnaString[i] == 'C':
            dnaString[i] = 'G'
        elif dnaString[i] == 'G':
            dnaString[i] = 'C'

    dnaString.reverse()


    return dnaString


def main():

    INPATH = './datasets/1cba/rosalind_1cba.txt'
    OUTPATH = './datasets/1cba/result_1cba.txt'


    try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            dnaString = data.readline().strip()
            result.write(''.join(reverseComplement(dnaString)))
    except IOError as err:
        print("An error occured : " + err.strerror)



if __name__ == '__main__':
    main()
