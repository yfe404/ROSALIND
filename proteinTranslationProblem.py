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


rnaToAminoDict = dict()
rnaToAminoDict["UUU"] = "F"
rnaToAminoDict["UCU"] = "S"
rnaToAminoDict["UAU"] = "Y"
rnaToAminoDict["UGU"] = "C"
rnaToAminoDict["UUC"] = "F"
rnaToAminoDict["UCC"] = "S"
rnaToAminoDict["UAC"] = "Y"
rnaToAminoDict["UGC"] = "C"
rnaToAminoDict["UUA"] = "L"
rnaToAminoDict["UCA"] = "S"
rnaToAminoDict["UAA"] = "" # stop codon
rnaToAminoDict["UGA"] = "" # stop codon
rnaToAminoDict["UUG"] = "L"
rnaToAminoDict["UCG"] = "S"
rnaToAminoDict["UAG"] = "" # stop codon
rnaToAminoDict["UGG"] = "W"
rnaToAminoDict["CUU"] = "L"
rnaToAminoDict["CCU"] = "P"
rnaToAminoDict["CAU"] = "H"
rnaToAminoDict["CGU"] = "R"
rnaToAminoDict["CUC"] = "L"
rnaToAminoDict["CCC"] = "P"
rnaToAminoDict["CAC"] = "H"
rnaToAminoDict["CGC"] = "R"
rnaToAminoDict["CUA"] = "L"
rnaToAminoDict["CCA"] = "P"
rnaToAminoDict["CAA"] = "Q"
rnaToAminoDict["CGA"] = "R"
rnaToAminoDict["CUG"] = "L"
rnaToAminoDict["CCG"] = "P"
rnaToAminoDict["CAG"] = "Q"
rnaToAminoDict["CGG"] = "R"
rnaToAminoDict["AUU"] = "I"
rnaToAminoDict["ACU"] = "T"
rnaToAminoDict["AAU"] = "N"
rnaToAminoDict["AGU"] = "S"
rnaToAminoDict["AUC"] = "I"
rnaToAminoDict["ACC"] = "T"
rnaToAminoDict["AAC"] = "N"
rnaToAminoDict["AGC"] = "S"
rnaToAminoDict["AUA"] = "I"
rnaToAminoDict["ACA"] = "T"
rnaToAminoDict["AAA"] = "K"
rnaToAminoDict["AGA"] = "R"
rnaToAminoDict["AUG"] = "M"
rnaToAminoDict["ACG"] = "T"
rnaToAminoDict["AAG"] = "K"
rnaToAminoDict["AGG"] = "R"
rnaToAminoDict["GUU"] = "V"
rnaToAminoDict["GCU"] = "A"
rnaToAminoDict["GAU"] = "D"
rnaToAminoDict["GGU"] = "G"
rnaToAminoDict["GUC"] = "V"
rnaToAminoDict["GCC"] = "A"
rnaToAminoDict["GAC"] = "D"
rnaToAminoDict["GGC"] = "G"
rnaToAminoDict["GUA"] = "V"
rnaToAminoDict["GCA"] = "A"
rnaToAminoDict["GAA"] = "E"
rnaToAminoDict["GGA"] = "G"
rnaToAminoDict["GUG"] = "V"
rnaToAminoDict["GCG"] = "A"
rnaToAminoDict["GAG"] = "E"
rnaToAminoDict["GGG"] = "G"



def rNAStringToAminoAcidString(rnaString):
    aminoAcidString = []

    for i in range (0, len(rnaString)-2, 3):
        aminoAcidString.append(rnaToAminoDict[rnaString[i:i+3]])
    return aminoAcidString


def main():

    INPATH = './datasets/2a/rosalind_2a.txt'
    OUTPATH = './datasets/2a/result_2a.txt'


    try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            rnaString = data.readline().strip()
            result.write("".join(rNAStringToAminoAcidString(rnaString)))
    except IOError as err:
        print("An error occured : " + err.strerror)

if __name__ == '__main__':
    main()
