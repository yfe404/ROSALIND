#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of G and C in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC ")) are:

# 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

# Minimum Skew Problem
# Find a position in a genome minimizing the skew.
# Given: A DNA string Genome.
# Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).


#
# Author:      feunteuny
#
# Created:     27/07/2015
# Copyright:   (c) feunteuny 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def skew(genome):
    return (genome.count('C') - genome.count('G'))


def minimumSkew(genome):

    genomeLen = len(genome)
    skews = []
    minimumSkew = 0
    minimizeSkew = []
    for i in range(genomeLen):
        skews.append(skew(genome[i:genomeLen]))


    minimumSkew = min(skews)
    for j in range(len(skews)):
        if skews[j] == minimumSkew:
            minimizeSkew.append(str(j))

    return minimizeSkew



def main():


     INPATH = './datasets/1fba/rosalind_1fba.txt'
     OUTPATH = './datasets/1fba/result_1fba.txt'

     try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            genome = data.readline().strip()
            result.write(" ".join(minimumSkew(genome)))
     except IOError as err:
        print("An error occured : " + err.strerror)

if __name__ == '__main__':
    main()
