#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      feunteuny
#
# Created:     28/07/2015
# Copyright:   (c) feunteuny 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from reverseComplementProblem import reverseComplement
from proteinTranslationProblem import rnaToAminoDict
from proteinTranslationProblem import rNAStringToAminoAcidString
from patternMatchingProblem import patternMatching


def peptideEncodingList(genome, aminoAcidString):
    patternLen = 3*len(aminoAcidString)
    patternEncodingPeptide = []

    for i in range(0, len(genome) - patternLen):
        pattern = genome[i : i+patternLen]
        rcPattern = "".join(reverseComplement(pattern))

        if "".join(rNAStringToAminoAcidString(pattern.replace("T", "U"))) == aminoAcidString:
            patternEncodingPeptide.append(pattern)
        if "".join (rNAStringToAminoAcidString(rcPattern.replace("T", "U"))) == aminoAcidString:
            patternEncodingPeptide.append(pattern)

    return patternEncodingPeptide



def main():

    INPATH = './datasets/2b/rosalind_2b.txt'
    OUTPATH = './datasets/2b/result_2b.txt'


    try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            dnaString = data.readline().strip()
            aminoString = data.readline().strip()
            for pattern in peptideEncodingList(dnaString, aminoString):
                result.write(pattern + "\n")
    except IOError as err:
        print("An error occured : " + err.strerror)




if __name__ == '__main__':
    main()
