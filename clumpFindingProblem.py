#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger)
# string Genome if there is an interval of Genome of length L in which Pattern appears at least t times.
# For example, TGCA  forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAaTGCAtgacaagccTGCAgttgttttac .

# Find patterns forming clumps in a string.
# Given: A string Genome, and integers k, L, and t.
# Return: All distinct k-mers forming (L, t)-clumps in Genome.
#
# Author:      feunteuny
#
# Created:     27/07/2015
# Copyright:   (c) feunteuny 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from frequentWordProblem import fasterMostFrequentsKMers


def clumpFinding(genome, k, L, t):

    genomeLen = len(genome)
    ltClumps = set()

    for i in range(genomeLen - L):
        for pattern in fasterMostFrequentsKMers(genome[i:i+L], k, t):
            ltClumps.add(pattern)

    return ltClumps

def main():

    INPATH = './datasets/1eba/rosalind_1eba.txt'
    OUTPATH = './datasets/1eba/result_1eba.txt'

    try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            genome = data.readline().strip()
            args = data.readline().strip().split(" ")
            k = int(args[0])
            L = int(args[1])
            t = int(args[2])


            result.write(' '.join(clumpFinding(genome, k, L, t)))
    except IOError as err:
        print("An error occured : " + err.strerror)



if __name__ == '__main__':
    main()





