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
Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.

"""

def patternMatching(pattern, genome):

    indexes = []
    genomeLen = len(genome)
    patternLen = len(pattern)
    start = 0
    end = genomeLen - patternLen

    for i in range(end):
        index = genome.find(pattern, start, end)
        if index > -1:
            indexes.append(str(index)) # indexes added as str to be more convinient for the print function
            start = index + 1
        else:
            break

    return indexes




def main():

     INPATH = './datasets/1dba/rosalind_1dba.txt'
     OUTPATH = './datasets/1dba/result_1dba.txt'


     try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            pattern = data.readline().strip()
            genome = data.readline().strip()
            result.write(" ".join(patternMatching(pattern, genome)))
     except IOError as err:
        print("An error occured : " + err.strerror)





if __name__ == '__main__':
    main()
