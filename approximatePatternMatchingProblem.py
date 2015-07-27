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
Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.


"""

def hamming(str1, str2):
    diff = 0

    for i in range(len(str1)):
        diff = diff +1 if str1[i] != str2[i] else diff
    return diff



def approximatePatternMatching(pattern, genome, d):

    indexes = []
    genomeLen = len(genome)
    patternLen = len(pattern)
    start = 0
    end = genomeLen - patternLen

    for i in range(end):
        if hamming(genome[i:i+patternLen], pattern) <= d:
            indexes.append(str(i)) # indexes added as str to be more convinient for the print function

    return indexes






def main():
    pattern = "TTGATGGGTCTA"
    genome = "AGCCAGCGCGATTCTACGGAGTCGAACAGAGTTCAGGGTTACCTGAGGCGTATTTTACACTCGCGTAGGCTAGTGTATCCTCAGTCTTGCGAGGTCTCGACGGTTACACCGCCCAGTGGACGACCGGTTTACGCTTTACGGTCGTACGATTGTGGGTTAGGAAGGTTTCTGACGACGGACTGGCCTCAGATAGAACGGACCCGTAACACCGGCGATGAATCGTGATAATTCTGGAATTTCCTGGTCGGCAACACTTTCCGTTGCAGTTCCGCCGACTACTACGTCGGGATGGAAAGAGCCCCCACGCGTTACGCCGTCGGAAGAATCCTTACTAAAGCGAGCGCCGTAAAATCGAACTCCACATTAGCCGATAACGTGCGTATAAGATGTTTAGATTACCCGAGGACGGGCAGGAGCCTCCCCGAGACTGGTCATGTTTGGTTTCGAGAGGCAAGACCGTTCGGTCTTAGCGCCCGGACCCAATGTAGTCTGTAAGACACGAGTTCCTAGCGCGTGTTGGGACCACTACTTTAATACGGGCTGGAAGTACGCCGCGCAAGCTACTCACCACAAATTTGTGAAGCCGCTTATTGCTCCTTCAATCACCACTAATGAGCAGCCCCTACTTAGCGACGCGGACGATTATGCGGACTGCAGTGCGGGTCCCTATCAGGATGGAATGGCTATGGGCCGGGTCCTTCAAGATAACGGGTAAACTCGAAATACCACATCGATCTCAAGTACGTCCGCTTGACCACCGCCCCAGAGTTTTGTCGCGCACATTGGACTACCTCGACGGTGCCACGTCAAGCTAATGATTGCACATGCGGTGAAATGGCAGGTGTTGTTCGTCGTGGTATGAGTAAAGAGCGTGGTCTACTTGGATTCCATGAACCCTTATGCGTCTGCGGAGACTAGCAGTGAAAGGAACACAGACGGGTGGGAATCTCCCAAGGAACAGGGTGCGAGACCATCATTCGCCTGCTAGCCAAACTATACCTTTTGACTTCCGTGGTGGCGGTAATCCATAAAGGGCCAAGTCTTAATAGAGTCCTTCGAGAAACGGATGCTCGTTCATTAACCTTGTGCTAGGCACACCTCCTCCTCAAGAGACCAATCGCCCTTGACCGAGTGTCAAGGCAAGTCCGGTCAATGCGAACAAAATCGTGTTGGTGCCCCGTGTTAACTTCACTGAATACCGACGACATGAGAGGCTTCTACATTATAGACCTCGCTTTATTACGCTCCCGCCCTCCGGTAAGACTTTGAGAGTGTTGCCACCGTTACGCCAGGCAGTTTCCTTGAGTCACAACACTCAAGGATTCGTAAGGAAAGCGGCACACCACGCTCATGTCGGATAACTGTCGGCGCAGTTCCGTCACGAGTCACGTGTGTCTCCTCAGAAGTTAAATAGCTGACAGAGGCAGATAAGTACCACAGGCATCGTTAGCGATCTGTTACTGGTACGCAGACTGTTAGACCTTTTGCAAGTTAAAATGAGAGAGCTCTGGTATTACTTTCGAATTAAGGGCTATTCTGAAACATTAACCAGCCGTTATGCTACACCTGTAGGTTTGAAGGTTAGTGTCTGGCCCTCAAGGCACTGGTAGCCGAGATGGGAGGGCCTTACAGATCTTGGAGCGACAAGCAAGTGACCTTTAGGCAAGGCTTTTCGTGGGGTGTAGTTGATAGCGTGGTATAGGAAGACTAATTTTACACCTGAGGCCTGAACGACGAGTGACCATGCAACGTCAATCATGCAGTTCGTGTTTCCCACCTCGCCGTGTCATAAATGTGTCATTTCAGTGCGAGCCAGAGGACTTTGTGGCTACCGTTTATCCCGTTGAACCTCGGGTGGCGCGTTAATGGTCTACAATGGATCGGTCTCAAGATTGGCTTACGGAAAAGCTATGCGGGACGCTAGGATTGGGTGTCGCTCAAAAACACGCAGAGGCCTCAATCGAGTTTCAGGTTATTCATCGCCTGTTATCTATCCAGGTATTCGACCCGTATACACTACGAGAGATAGCATGTGAGGCTGGCAGTGCATGTTCCGGGACTTTGCGTACGTTACATATGAGTGAGCTCTGATCTGGTTATATGTGCAGCATTACGGACTTTCTTGTCCCACTCATGGTGAGTCACTTCCCGCTCGTCTATCCTTCTTATGAGGAGGGCCCCTCCCGTCCAAGCAGACGGCCAGCAGCCTCTGTGTTTCTGTTTAAACCTGACTGGGACAGCGTGGCATCGGACTATACAAGGCGGTGGGTCAAAAACCTTAAACCTATTAGCCACAACATGCCATAACAGAATAATGAACAACTGGCAGGTCGGTAAAAAATGACCATCACGGTGACATGAGAAAATCGTATAACGACTCTACAGGCTGTAATAGATGCCTTGCGGATGTTTGCCAAGCCGCTCAGCACCTTTACGTCACGGCAACTAGATGGACCGGCGTAACCCTGACCTCCAGGATACTCAATTCGGGTGGGCTTGCATCGCCGAGAAAGTTTGTGAGTGTCCGCTTTTGTTTCGGACTGGAGTGACGCGCCTGTCGTCTTATGCCAGTGATGATACGATATTAGTCACTATAAAGACGACTATATACTACATCCCTACATGCTCTACAATTTTAGATTCCTATGCTTCGGCTAACGATACCGTTAAACCCACAGATGTCACGGCACCCGCTCGTAATCTAACACATTCTTAGTGAGATACGAGCTCTTTGCCACGAGACTCTGACCGAGTAGGGGGGGTGCGTCTCACATGTTCCAAGTCCAGTAGCCGCCATAGCCGGAACGGTGTCCGTGCAGTATAACCCCCGGTTGGTGTCGCCTAGACCTTCGATAGAGAGAGCGGCTTAACTAATACACTGGGTGATGTAGAGCGCGTGCAACTGCCCTTGCCCTCCGCTATTTAGTAATGTCCGAAGCATGAAGGTTTAGAGCTTCGTACGACCGGGAGGCCCTGAATCAGTGAAGAACCAACCGACTCAACCGTGAAGATGGTAAACCGCTGGAGCTAACACTGAAGCCGAGTGACCAGGCTATCGTCAGGGATTCATCGATCAGACGGGTCGATTCCAATATTAATGGGGTGCTCGGCTCTGTTCTTTCCGCATACGGGAACAGCATTATTGGGCGAACCGAAGACTCCTAATAGCATGCTAAAGCATTGGGGCCTGCGGCATTGGCGGGGCTTTGCGGTCCCTTCAGTTTAAAAACCTGGTCCTGAGCGTTCGGCAACTTGACATAGGGACCAAACGAAGTCTTTAAACACATCAGCCTCGATGCGCTTGAGTAAGATACTCCCCCTTAACTAGCGTGTCTGTCACGCGTTCTTTCGGAGAGGGGCTGACTAGAGCGCGTGACTGAGTCACTGACCGAGCCCTGCGTGCTTCCCTGGGTAGGTCTCAACTGAGAGGTGCGTGGAACTGCGGAGGGGGGCTAAAGAACTAGTTACCTCTGGCATTCGCATCACCTCTATCATTATACTGCAGGTTTGACCCCAATTGTATTTCTAGTATACATTATGGACGCCCCGTGTTCGCTGTTCAAAGCTAGAGGACATATACGGTTAGTTGTGCATCTCAACCCAGGGTATTAGGGACCTAAATGCTGACTAAGGGGCCGGCAAGCCTAGCGATGGCCAACCTAGCTTCATAGCCTGCCACCTCCTACCATGCATGTTCTGGATGGGCCGGTTATGAGAGGCTGGGACGGTTTACCGATCAGCACTCGGCTCCATGGATTCATCCGGCGATGATTAAGAGGCCGGCTGACAGCTTGGTCGTGCGTTCTGGAAGGTAGCCTTGCAAATAAACGTTCAATACGTTAATAGTAGTAAGTACGAAGCGCCCCAACAGCCCCCCGCCTGTCTGACATTGAGGGCGGTCCAGGCTATGGGGACAATACCAATGCTTACTGGAGCGGCTGCGGTCTAGTAGAGACGGTCGCCTACACAACTAGAAATCGGCAGGCGCAAAGAGTACACATGATGGACAATGCGGGCCGCCTTTGTTATTGCCCGTTCAGTAGGGGATCGCACATGACGATACGGTATTAGTGATTTGATGACGTGCCGGCGTACCATCCGCGACACTCTTTTCCTGATGATGTCGCGCAATGACGCTCTCCTGATGTACGCACAGCTCATATGTTGTAATCGGGCATGGAGATCGAAAGGGTCGCCTCGGAAAGTGGAGTGCGGAACGTACCAAAGCACGTCCCAAAGTTTTAAGGGTACCCGACTGCATACACGCACTCCACAGCTTGTTTGGCTACGGTCTCAAGTCAAATGGACTGTTCAACAGTCAGTATTGTCCTACTCTAATAACCGTCGGAGACGGCTTTAAGTTTTGCGGTTGTAACCTCGCACACCTCAATACAGAGATCCATTATTCTACGGTTTACGCGAGAAGCAGAAAGCCAGACCAGATCCGTGCCACGCCAATAGCGAACACAAGACAAATAGCTTTTGGGGTCAGGAGTCCAGGGATAGTCGGCGGCCCTAAGAATTCATGTGTGTCCCCACGTAGTAAAATGGAAGACCAAGTAACGATGATTAGTGTTTGTCTCTAGCTCGTTGCTACACAGAGACAGGTTGCCACTCTCATTCCCGTAAACCAAGGCCCAGTTTCATTTGACAAATTTGATTCTGAAGACAGGCGCAGTCCAAAGTCGACACTTTAGTCAACCGCAAGGTGATTGTACCTCCGGGCGTGGGAACTGAGGCTGTGTGTCTGTAGTAACGTATCTGGCCAACGGTCATTTCGCGAATATACATAGCAGTCACCAGGGCATTTGCAAACGCCGCAGCAGGCAGAGTGACACCATTGCCAATTTCTCGTTGGCAGTCAGACGGGTCAACCCAATGACTACCGTAACATCGATGTTAGATGATAGTGACGTGGGAGCGTCTGTCCTCAGGATGCCAAATTCCTGGCAGAGTCGTGACCGAAAGCAGTGCAATGTTACGCAGGGTGGGATTGATCTACAGCAGGAGACCATCACCTCGTACTGTCCAGCTATCAAAGTTATATTTGTGCCACTTCATATGGTAATAGTAGTGCCAATTAGCCTCCTCCGAAATGGGTGGGCATGGAGTTTCTAGGGCTACTGATAATCAAACAGAAGGTACTTTGTATCAAGCAGGTAGCCAGTCCTTTTTTTCTGACACAATCCAGGTACTTAAGGTGTTCCCCAGTACCAACGCTATTTAAACAAGTCTTCCCTAGATCGCTCAGGGTCAGATATAAATTCTGCCTCGCCCCCGGCTGCTCCACCAGGACAGGTGCGTATCGTTGTTGTCTCCTGGCGAAATCACAGCAAGGGATGCCCAGCACACCGGGCTTCCGATCGTCCAATTCGTGGGTTTATCCCCCCTAGCGCACCACCGGGTCGGTAGCCCCCTGGACTAAGGTCCTCGCCCTCGCACGCCAATGGAAAGTGTTGCCAGAATATGTGAGTTACTGAGTCTTGCGAGCGAGCCAACAGACGAGGGCAAAGCATCTAAGTTAAAGGAGTATGCTTGTATTCTCTGGACCGTGAGAGAAAGAAGGACTATGAGCTTGCGGTGAACCTCGCTTGTGAACCGGGACTATGTCGGTGTGCGACAGCACAGCCACCCTGACAGAGGTTAAGAACTCAATATGATAACATTCGTAAATATCCCTGAATATGGTGCCTTATATCCTTTCATTTTTAGAAGTACTCTCTCAGAAGTATGGCTATAGAGCTTACTAGGGTTTATGGCCGTTGCTCACATCGTGTTCCAAGGAGCTATACGAAGTGATTTAGCGCCGTGCCTACGCGGAGATGCTAAGTAGGGAACCCCATCCTTGCACGTTCCCACCAAAATTCTACAATACAGTAACGAGGTTTAATGTGTAAACCCCTTATGTAGATAGGTCGTTGGTAGTTTCCTCCACATTGCAGTCGAGATGGACTAGTATCTTGGATTTAGGGCTAACGGTACTGGTACAAACGGGTTATCTGGTCCGACCCGTACGCACACACGCTTACAATCGGGATTTCATAGCTCTGTCTGCAGAACAAGATACTTGGCGCATTCCGCAAATCGAAGCTCCTAGGGGGCTAACAGTGCCGTGCTTATTATTCTACCTTCCGACTCTGGGCATAACACATCGCCGATCTAAGACTGTCGTGCTCCTGAGACGCGGCATAGTATAATGGTAGGGGCAGTGCGAGGCCTAATCCTATCTGCGACGGGCGCCCATCAGCACTTTAGGACTCCGGGTCGGTCAATTACTGAAAACGCTGAGCCGATACGAATTGACTCTCGGGACGGTGGCTGTGCCATCTAAGCTTATAGGTAAGACTACGGTGGCGGCACTAAGGAAGCGGGCCTAAAGGGCTACCATTGGCTGCCCCGGAACGTAGGGGAAGCCGTGGATGCAGGGTATGAACAGAATGCGCGGTCCACGTGAGTGTCGCGAAGATGGCACTGGTCAATCTAACTTCGTATTCTTGGGAAGTTCAAATCACTAGTTTTGAGCGAACACGTACTCCTGACCGGTATCCAGGTGTCGCGATTACCCGAAACCATCTAATAATTGGTACGCTCAATACGATCCTTCCGAGTGAATTGTTCATGAAAATTTGTTCAACTTAATAGTTCCGCCTCGCTGCTTCCGATCACATTTGCGGATACAGTATACGATGACTCGAGTTGAGCACCAAAGTCTAACATCTGTAGTTCCGGGATGTCCCTCTTTGAGTGCCCGTGAGGCCTGCAACAGCTTTAATCGTTCGATCCGATTCTGCCACTTTAGAGTATTCTCTTTCGCCAATCGGGAGCACAGAGAGAGAGACCCAGGGCCGTACCGCTAACCACAGTCTAACTGGAAGGGCGTCTGGACCCTAAGGCGAGAAACCAAGCCGTCTAGACAAACAAGTAAACAAGAGAATGAAAGCACGACTCCAACGACTGTTTGAAAAGCAAGTATTTTATGGTCCTACACCTTCTTGGTCCAACGGACCATAGGCCGTTGATCACTTGATGCGTACGGATGGCTTATAGACTATCTAACTATCAACCGGTGTTCTTTCTGTCCACCGGCAAGAATGACACTCTCTTGCACCGGCTTTTAGCCTAGTAATGCCTGAGATCCACTCAGGACTAGACGATAGCCTTACAGTCGCGGGCAATGGGGAACCATAGCGGGATTAATCTCTAGGATAGATCTATGAAGTGCGGCTCCGAACCTTGGGGTACCGGCTGGGCAACGGATTGCGTCTATCCCGTAGCCCAGCGTTGGCACTAGACGTGGATTCGGCGTTTTTTGGACAACTAACTGGTGAGCGGCCTTAGGACCAAGCGTTCCCGATAAAAGGCGCGAGTGTTTAACCGGCGGTAAGCTCTAGTAACTAGTGCACTTCCTCGCACTCTTATTACCAGTCCTGATCCGCGTACTTTCGCGACCCCAAAGTGACATCAATATAGCTATCGTCCGCTAGTGATCGGTCAGCGGAACGGTCCGTGATGCTCCCAACCATAACTGAGGTGTAGTCGAGCTATGAGTAATACTAGCATCGTTCCGCGCTACTGTACATGCAGCTGCGAGCGCTCAACGTACTCACCTTTTGTGAGCCAAGATGAGACGGACGTCGTCCATGTGGCCATCGAGAAATATTCTGCCACGGCCAGACCGGAAGTCTGCGAAGGGTTTCAATTAGCAACGTAACATCCCGACCTATCAAAAAGTTGAGGACAGCTAACACAGCAGGACTGTCGGGCGTTCACAGGACGAGGGTGCACAGACGAACTAAGCCAGGTGGTCGGTTCCACACAGCTCGGTTCAGTGCGCCTAGTACTCAGGCGTTCAGACCTGGCTAGGCATACCTTGCACTGGCGGAATGGGGCGCGGATTCAGTATTAGATCTCACGAGTGGTACTTCCAGTTGCCCCTGCGCCATATGCCCCACCATCAGACAGTCAGCAGGGAATCTTAGGACGGTACACGAGCTGGCACCGGTACTTATAGCTCGGAGGTAGTACCTATAAGGGAAGTATAGTTAGCGAGCCGGGTCCATGGATCGGTGAAACTCGTTAGGTGGCCAGGAGCCGACATTAGCTCGTCGGCGAGAAACACCGAAGCGAGCACGCTACTCGTTGATACGGCGCTGTCTCTCGTTGGTGTTCTCCGCGGACTATCTATCGCCAGCAGATGTCCTTCTTTATACCAGGAACACCGCGAGCTAGAATGGAACTGCGTCACAGACCTATAGCTATAAGGGAACACCCGGTATGCAGGAGAGGGAAACAATCACATCGATTCCGCTTCATCTCGCGGGATTGCAGCACGGGAGTAAAGATTAGTTGAGGAAGGACGTTTCCCTAGGATCCGCAATGATATAGAGTTGGCCGTCCGGTTCTTACCTATGTGTTATAACACGGATGGCCCTCCCCGTTAAGAGAGACTCACTCATTGCGCGACCTATCATGGCGACGTGCTCTGTTCCCCAAGCTAAGAATCATATGTGAGACTATTGAGCAATCTAGGGTTAGGCCCGGACCATGCGTAAAATTTACGGTAAGCAGATGCTACCGATCGCAATTTACTCGATACCTTAATCCAAGGTCCGTTCCCCCGTAGCAGCCTGGATCATTTAGTGTCTTCCCATGTCAGATCTACGTATAGTTCATGAGGGCCTAAGGGATTCTCAACCCCTTAGTTGTGAAGTGGCTCCACTGTTGTTGTTCTTCGACAGGCCAGTCCCCAAACAAGCGATGGAATACTCTTTATGTGACCAGTCTTGTTTCAGCCGGAAAGTTTCGTTCGACCTTAAGATGTACGTGACGGGCACCTGTCGTCCGCATAAACTTTTCCTTAGCTGGGGACACATTAAGCTCACCAAGACCCGTTAAGACTATTGGGTATATGCAGAGAAGGTAAGATGGGTGAGCATCAACGAAGACCCGGTTTGAGTCGGGTACAAAGAGAAGAGGACAACTGGGGTTACCCTTAGTGGAAAGGTGGAATTCTTTATGACAATATTTAGAAAATATCTTGTTAGATAGGCGTGCAACACTCTCAACATACCCCTGCAGCCAACCAGTGCAGAACTTTCTAACGAGCTGCTCCATGATCAATGGAGGGAATACACCGCAGTCACATTCGTGGTTTTGTGCGGCTGTGTGTCGTTTCATTGTTAGGCGAACCGATGAGACCAGTATGACACGCAAAGGGATACGTAAACCCCGGTACATTCCTGGTAAGCGGGATTAACTAACAAATTCTACAGCGCTCTGAGTACTGGTAAATCACATCAGAGATAGAATCCTGTCATGTTGTTGGAGATGGAATCGGATAGCTTATCGCGATGGGTTAGAAATCTAGGTCATCATCCCGGGCCGAGCGTGGTGAACGCTTCGGTATAACCTAACACTGACCCGCGTATCATGTTGCGCGTGGATTGAGGTACCTGCAATTACAGTTCATCAGAGCCTACACTCACAACATGCATGGGTTCTTAAGAGGGAACAATACGCGACCTGAGGACCTGCCATGCAATACGGTAATTTTCCTCCTTGACACTAATTGCATCCCAGCATATGGGCTCGCGCTACGGACTTCCCTTGCTCGGCCCAGAAGATAATCCAACGACGTGAATAATTACCTCTTGGATTCGTGTGAATCGAATATACTAGAATGTTTAAGGCAACTATGAACCTTGTCCGAGTAGCCAAATTCTTAACTGTTGCCACCGATGCCAGGAGACTAATGTACTTGTGTAACAAAGGCGTATTGCTCATCGGCTGCAACGCACGACTGGCTATTAAAACCGTATTGTGGTTTAGACCTGGAATGATCAAGTCGCCAGCCGACGGGGTGACACGGACGTCAACTATTAGAAACGAGATACCTAGTTCTGCACTACGTAAAAACTCAAAGACCCTAATGTGAGTCTACTCAGGCCAGGAAGATCGGGGTCTTCTGGTCCGTGATAACGCTGATGAGTATTTCTGATCGGCCAAGACGGCACCGCCCAGTTAGTATCGTGCAAAGGGAGCGTAGGACTTACTCTGAAATCTATCTAGTACGGCCGCCTCCACCGTCACAGTGGTCTGAGACCCCAGGCCAACGACAGAGAGTGTTGACGCTGGTTCTTCGTATTAGTACCACTCCCACTTAGGTGATGTTTTGCGCTTGACCGCCAGGCTCCCGACCGGATTCCCGCTTCAGGGCACACAAAAAAGACAATATATCTGGGAGGTGTTGGCACGCTTAAGGCTTTGGACGTATGGGATACAGGGGCTGCATTCTGCTCCAACCTGAAGCAACTTTTCGTGATAAAGGAGCTTTCAAGGTTCTGCAGCACATGATTTGACACCCCCTAGCAGCAACGCGGGTCGGGGATGGGTTCAATGATTTCGTTTGTTATGACGACCTCTCCGCTTCTGACCGCGCCTAAAATTTCGCATGGGAATAGCGAGGCTAGGTGCAAATACCCAAGGTGATACTTACTCAAAGCGGTGGGTATGCAGGCAGTAACTTGCTCAAGCAGGGTTCGCGCGGGCGTATTGGTTGACACCTATGGCGCTGGAAAGAGTTGAGCGGATACTGCATTCCGACCCGGGGGCGACAGAGTGATCGTTCCGTGCCTACTACTGCATCTAGGGACAGCTCGCGGAATGTATGATGATTAGCCAGCGTGATTGTTTTAAGGCAGAAATGTCGGGTCATCGAGTCGGCTGGAAGACCTTCACCGGCGTTGAGTGAGACGGAATCCGTGCAAAAAGGCCATAACGGTCGATTCTCCAGAGAGCTACTAGCCTCGAGTTCTTTCTTCCCAGGGCCCTTCATAAAAATGCTATCTTTAAAGCCACACAAAATTGGGGATGGCTCGGTTTGTTGAGTGGGTCTTGGTCTTACCTACCGGCGCCTTAGTAATACCAATAAGGAAACAGTGTACCTTAGGGTCTCTGCCGTTCTTAGGATAGTTTTAGGTAAACTTGGGTACCCGGGAAGTAGGTTAGTCTTGCTCTCAGATACCTCTTCGTCTCAGCCGTTAGAGAGCGCGTTGGTGATGACGAGTAAATTGACGGGTTCTCCACAGTTGTCCAATGGAAGTCGACTGTGGCGTCGTTAAGGCAGGCATTAAATAGTCCTGGGAAACGAGACTAATTTTTATGGAAGACGCGATCGTCGACAGATAACTGCGCACCAGTGTTCCAATTGTAGGATGGTAAGGTGGACGGACCCCGACGCCAAAATTCCTTTCCACATACCGATGTCCTCCTAAGTATAATTGCCCAAACTCTGTTGTCGACTAGACAAAAATGCCAACACTGCGGTGCGATTCCTCTTCACAGATCATGGATTCTGGGCGGCTGGCAACATAGGTGCATGGCACCCATCGAGAAGCAACGGACGTTCAGAGTACCCCCTCCGTTTGATACTACGATGGGGGCCCGTCGAATGCGCTAATCCACGGCGCTAAAAGACTGGTCACAGGATACGCGATTAATGAACTGTCGAGAGTCGATTCCGTAGAGTAAAAAACGCATAGGAATTCATATGTTTCCTCCACGTTTCCACAGAGGGGAAGCCTCCTATTGAGGTTACCAACCTCGTACTGTATTCCCTGTCGGGCAAACACTAGAACTTCGGAAGTGCCATTCCATGATTTGAACCCCGCCAGGGTCCTCAATAAGATTATCTTGTTGCCGGCTAAGTTTGAATAGTATTGTACCCGCTTACCGCAGAAAATTGGGGAGGTCATGACACCGCCGCATGACGCACGGTGTACTAGCAGTTTTGATATGGCCACTGACCGTAATACCTGTAGAAGCGATCGATGATTGAACAAAAGCCGCCTCACTTGAAGTGTCTTGAATATCTATCGCCTCGTGGGCCAAAGGGTTGACACTCGTAATACGGAACTCCTGTTGATGGGGCACTAAAATGGGCCGAGGGGTTACATACTATTATGCCGAGAAGCCCCGGTATATAAAGAGGACAGAGTCTGATATAATCTTTCCTTCATAATCTAGCGGTAAACAGAATCAATACGGTGTCCTGGTCTAGTGAGCATTATTACTGCCGAAATCCCGCATCCAGCAGAATTCGTCCCGCAGAAACCTCCACAGGTGCAGAGACTCTCAACATCACTTATTGCTCCCCACCCCGCTTAGCCGGATTAAGCCGTGCAGGAATTTTTAGCGGAAATAGAAACGTTCTCTTTAGACATGGTAGGGACGGGATGTACCACATAAGGCAGTTGGATCTCAGCGTGAGACAGATTCTAACTCCATTGCCTGGCCTTTTAAGATATAGGCTGCGGGCGCACTTATGCTTCGGATGGATCCGTATTGTGGTTAGCCGTGTCCTCTGCAGTAGAGGTATCGATAGGTTTGGGAAGGAGGTTAAATCATTAGGTCAATATCCTCATGAAATTGCTATTTAGCGTATTGGATAAATAAGATTTTTAGGCTTGTGGGGAATGTCGCGTCAAGGATGCGACCACACAATACTCACGACCCTACAACGAGCAACGAGTATGTATCCTACGTACCCAAGTTTGAAACAGCTTATGATACCCAAAGCAGTAAGGAGTCGTCAGTCGGCACGGACGCGCCGATCTAGCTCCTCTGCTCCGCACCGCTTTTCACTGTGACCGGGAAATCATGGTCGCTTCTGAATTGATAGATTAACTGACCTATCGTCGTGGCGGCCCCGGGATGCGATGTCCACGTGTAACTCTAAACATGGAACACTACCCAACCAATACACCTCTACTCAAGTACGGAAGTTGATAGTAGACTCCGTAACCAAGAGTGATTAATCTCGGCACTACAGACTCAACTCGCTTCCAGGGCGGGGATAAGCGTGGACTGGACCTGCAAAGTAGATACATTCGCCTGCTGTACCGGGCTTTTGCGGTTATGGTTGTGTGGTGGTAGCACGGTTGAATCCTTCGACGCATTGATGCTGATCGGTTAGCTACACGCCCTAATTTATGGGTGAGGAACCACACACTGCCGGGCCGTGTAACGCACCAGTTGAATGCTATTAGTGGGTTTATTTATGTGCGTGGCACCCAACGTCTGGATGTGAAATGGACACCATCACAACGAGGGGCGAAGCCCGGCAGATTTAAAACGCGCAAGCCTGGGTAGGTTTCTGCTGAGCAAACCTCACGCGACGCGGTATTCGATCACCACAAAGTTTAATCTAATCGTCCGGAATCACAGGTCTTGGTTTATAGCAGTTAGTCGACCAAAGAACGCGAGTACCGTAAACCACCAAGCTAGTACCTCATGATCAATAGTGTCTAGGCTCAAGTAGCATCGGGTCGAGGCGCGTGAACATGCCGCAGAACACCCCATCAGTACGATAAGTTTCGTTTTCGATTCGATAATATTGAATTCTGAGTGAGGACTTTGCGGAGTGGGGAAGCACTGACTGTGGGTAGCACGCGCGTATCCCGTATGCGGCAGTGTCCGCGCTGCCAAAACGGCTTTTATTTCACGTACTATAGTGGGGTGCCGTGTGAAAATAGTCCCCTCAACTGCATCTCCGGGGACGTTTGAGATAAGTGCCTAGCTAAAGTACTAGTATGGCTCTCCAGTAACCGGAATGAAGGCCTAATATTACGAATAGCTTGTGTAAGAGAGAGTCTTGATGGGATATCACTGTTTGATGATAGCCCCAGCCTTGTCTTAAAAGTTACCTCAGGTCTGCTACGCGTAGAAAGGATGAACACAGCTACCGCCACTTCTAGGATTAATTAATCGTTTGCAAGCACGAATGAAATTGATCAGGGCGTTGGCATACCGCTATCACTAGTGGCTAGGCACTTGACTCTCCGCAACGAGTGTCCATAGCGTTTAGATGTTTTCGGCTGCCCAGTTTTTAGATCACTAGAAGGTCCCCCATGGTTTCGGAGGGATCGCGTTTAGACGCCACTGAACTACCTCTAAGGTGCTCGTCCGCTAGATGGTGACAGGAAAAACAAGTCCCCTAGGGGAGGACTACTTCTGTCATTTCCTGACTATTAATCCATGTCACCCCACGGAGTAGGCCGGGAGGTTGCCCTCGTGAGTTGCCAGAGGGCTCAGGCTGATACGCGTACGTTTCACAGTTAGGTTGAGTAGTTGTAAATGGACTGCCCCTGCACGTGGGAGACCCGGTAGCCCTTATGTCAACGAAGCTCAACTATCCCGCTGTTGGGAGGATTTCTCGCCGCAGCAGGTCTAGCTTTGCTTTGAGGACGTGCCTGCGGTTCACTGTTGGATTCGACCATATGAAAAAGATAACAGGTTAGGATGAGCGTCGCTATGACGCGTTTCTCGTCCCCCATAGTGGCTATTAGGAGTCCGGGGGGTTAACAGCAGCACATATCTTCCAGCTTAGCCGTCACGACAGGCCTGGGAATCTCAGTTAGGGTACTAGGCATCATCGCTGATTCAATCGCCGATGCTAAAGTGACTACGGCTCGGAGTCTCGTCACCGACATGAGAACTCATCCAGTCGACTGGCACTCATTATATTAAACGAGATCCAATGTGTGGTATGGTAACGCTAGTCTCACAAGATTAGTGTAGGCCGCCACGCGTAGGAGCGGTAATCACGTCCCGCCTCATGGAATCAACGCAATTAATCGGCCAATAAATTTCGCTATCCTGGCTCAAGCTAGGCATCAAGTGGTGACTGGCGTACCGTAACAGTAGCCTACACCGAAGTCTTACTATCTAAAATGAGACGAATGTGCCTGTCCTCGTTACGTGACTCCGAGTCAATATGAAATTCGGTGATTGGACTGACGGTCACGTCCTGCGGTCTGTGTGTCACATACTGCTAACGCATCATAAACGCGCAGTGCTCTCCAAGAGTCATCTATCGCTGCTTTCTTTGTGATGGATCGTGCATCACGACCGGCCTGGGTCGTCGTGTCAATCACCACACATATTTTGATTATAAAAGGCTTAAATATAATAGCGGCTATGGCGTTCGGTTCCGGATACATCTTGGCTGCAGTCCCATTAGAATCCAGTATCTACCCTGTATGTCCCTCTGGCTGTCGACGCGCCCATTATATACAGCCCTACTTTCGTAGCCCGTGAGAGGGGGGCAAGTGGGCGGCACCGCATGTTCGCACATGCTAAGCCCGGGCTAATATAACTGCTATTTCCTACCCGTACAATCCAACCTTATAATATAGTATGGGTTGAGAATCGAACACGGTGATCCTTAGACCGCCGAGTAGGCCGGGTGGTAGTCCGCCTGGGACGTTTACAGCGAGCAGCAGGCTGTCTTTCTCACAACGGACACCAAGGCTTTCGGCGGCAAGACTTACCCAGAGCGGTCGTGCCCTAGAAGTCACCAAGAGTTTTGGTCGTACAGTCTGAAGGTGATTCGGTTCACACAGTCGGGGCTTACAGAGGTTTTAATGCCAGCGATTAGGCTGTCTGCGGTAGATAAAACTTATGATTCCTAAGTGATAAGCTGCTTTTTGCAATTGAAAAACTGGCACATAGTTTCGTGTCTATTGTCTAACCTGTACAATGGTTCAGAATACAATTCAACTAGAACTTCGGTTGATAGTTGAGTATGTGGCACATGTTTGATTGCTGTGCACAGGAATCCAACTAAACTTATTTCAGTAAGTGCATATCAGCTCAAGATCCATTGGTCGCCAGCATTATTTCGTGGAAGGCGCGATCTTGTTTATTTCCGCCTAATTGAGAGGGTGCTATCGTAGTAAACGTGAACACGGGGAACTGTGATATATATATCTGACGATTAAATCATTTTGGATATTGCCGGAACAAGCCACGTTGTCGTAGTACGATATAGTTGAGAATAATTCTGGCTAGGGCCTCGCCTAGATGTCTCCGATTTATCAGACTAATCTATCAATTGTTACCTGCAAGGCGACAGTCTGGGTGATGAGTGTAACTAAGCTTATTGAAAGCTGCTGTCCAATCATACGTCATACTCTATGTGCCGTGGTTAATGAGCGTGGAGGATTGAGGGGTACCCTTTAATGTGTACGACCTCCCCGTATCTAAGTAAGTAGACTACGTCAAGTCGGACCCGTCGAAGGAAAAAGTATTAAGAGGCGGGCTCGGCAAGTCCCTGCACCTAGAGTGCGCGCCATATGAAGTGACACCCTCGCGAAGCCTTAGAGGTAAGGTACCTAAGTCCTTGATGTGTGGCTCCGAAGTTTTCGGGTTACCGTCTCTCTAACGCGTCGAGTTCTAAGGCCGCTTCACGAGCCGTACTTCCGATCTTGAAAGGCACCCGTTTGCCGCATGACCCGGAACTTCATTTACTTATTGATAAAGGACTGGCTGGCGGGGCACGAAAATTCGAGGGGCGCGTAGTTTATGACACTCCTAGATAGTATCTTCGAGGACCTCACGGACCTATCTGAACGCTGCCAGGCTTCATGGGAAGCTTAATATCGTAGTTTCCACTGGGTGTCGAGGCGTGCTCCGCTCAGGCCGAGGGTGCCGAGGGTAGACCGGCTTCCTCAAGGTGTCGGCCGCGATTTAATCTCTAGTCGAACGGAGTGGATGAATTTCCCTCGGTCCTCAGTCCATGGACGCGCAATTGGCGAGTGCACTGACCGAGTATAACGGCTCCCTGGAATGGCTGATGATTCGTTGGGATTCTTAACAATTTTTTCAATATATGTGTCGACGGCCTCCGCAGACGAATATAATTCATTAGCGTTTGCTCAAGGCGTGCGGGTATTATGCACATGTCATGCGCATCTTAGTTCCACTGGGCATTCAAATCTTCACTTGATAATCTGCATATATTAAGAATTACCGTGGCACCTATCGTAACAAGCTATACGTAGTATATAGATGAATCAAAACTGACTTGGAGGCTGAAGTGTTGCGCCTGGTAACCAGGTAGGACATGTTATAGGCGCTCACTGAGGACTGAAATATACCTGTATGGTTCAGGATAGTTCGAGCGTTCTGTGGTGTCAGTGAGGATTTCATGGTCAGTGGTAGTGGTTGAAACCCAAACTCTACAACTACGCTTGCTTTCAGTCCTTTTCAGTATCCGGGCTCAGCACATGGCCTCATAGCAACTCTGGTAGATGTGATGAACTTCCTTTGGGGGGTCTGTGTAACATCCGTAAACGATCTGGTCGCACCATAGATTCGTATATAACAACGCGCGAGAATCTCGAGCTTAGTGTGTCTAAGGGGACACCGGCCAAGTAGTGCGGTCCTTGCCTAGATATAGCTATGGTTGTTCCGAGACATCCCATGGCGGACCGGTACTATCATCTGCGCCGCTCTCAAGCAGAAAATGATGCAGATGAACTCTTGGTTTAGTTACAAGTGCGTGCACGAGGTGTGCCTTTGCTCAGCTTTCATAGTGTTGCGGGAAACTCTGATACTTTCGCATTCTGTACATTTCCTTGAGGATGGCGCGAGTGTCAACCCATAAATAACCCATTTGGCCCCCGGGGCGCCATGGACTCGGCGGCTTTGTTTGTAGGCAGGCCGCGCGCCCTCAACCGGAAAGTTTTAAAGTACGCGCCTGACATCTGGTTGTTAGATTGCCCTTCACTATCCAGTCTTATTACCAGGGCGCCGGCCATCCCTTATGGTGGAACTCTCTTGCTAAAGAGTGTAGGATGACAGCGAAATAGAAGGATTATAACGATTGGTTAGTCAGCTTCCTCAACTCCAGAGTTTCTTATGTCCGCCAGTTTGATCATTCACCCTACGTGGCGTTCAGAGTCTTCGCCTGCTACGGCAGGTTGCTTACTGTATTTCTGATTACACAAATAGGAATACATGCTATCAGGCGAACTACCATTTGCCGTCTATACGACGCTAGCCATTACGCTGCTTCTATGCGGCTGGACCACAATTAGTGGCGGTGCCTACCGTTTCGCTTAAACGTTCGCATGATTTCGGTCAAACAGCTTCACACCTGTTGCACGCGGATTTTTTCGACTATCAAGCTTGCACTACGTCTCTCTCTGAAGCTGGGGCCAAAATGAGTTGCGTTGTCAGGATGAGGCTAGGTTGAACAGATGCAGCATCACCCGGACGCTTTCACATCTCAAGCGGAGAACACCGAGGTAGCAAACTCAAGTCGTATGATAAGAGCTACTTATAAGCCGAGGTCATGGGACCTTGGTTGCCATTCGCCATCCTAATTCGTTACCGTTGCAAACGTTAATACGGAATTAGTCAAAAGGCGATCAACGCAGCTTTGAGCGCCTCAATGTCCCACGCCGCTTCAAGATCCAGACACACTTCCCATAGGGGGGCTTAGAGTATCAGGTGCTATGTTATTTGGGTTTGCCAGATTTATTCACGTATACACCGCTGGCTGTTTGACTTGCGTGGGATAGACCCCCGTCGTCTGAACGCAATCGTATCACCTAGCAGTTTCCCTTCTTTAACAAAGTTCAACCCGGATAGTTTTCATACATTAGACGAATTCGATCAAGCTAGTTCTCACCACGCGCCACGAGCTGCCAATTGAACCCTACGAGTCATTTCCCCGGCGTCAACCTATATGCCGCGCACCTTACGGCTAGACGACCGTGCCGTTTTAACAGGGAGTGTTGAGCAAACATAGGCACGTGACCTTAAGCCTGTAGAACCCTCCACGCACATCAAGTCCACAGTTACGCCTGACACTGAAGGATGTGGTCAATCGATGGATAGCGCGGCGTGCTCTTACGGCCGCAGAACCGTCAGCTTGTTTTGCGCTAAGAATCGCCTAGCCTACAGACCGACTTATAACTATTATCACCAGCATACTTTCAGTGGGGAATGCGCCCATAATTAAACCGCACATAAGGGGGTCACGAACTAGCGTGCGCCTAACTAATCCAGATTCACCAAACCCCTTGACAAGGAGACGCGCAATGATTTGCGCCGACATATCATAGGTGAGACGGTCGAAGAAGCGTGGTCTTCCTCAAGCTTTTCAACCACTTTGCGACAACGTAGCCAAGTGGTGAGTCGGTTGAATAGGGAGAAGCCCGTTACGCCTCTGCCTGCTCCACGAAAATCGCGAGACAAGTGCTATACTGAGTAGGAGCATGAACATTAGGAAACTGGGCGAAACTTTACGGGAACGCGCCTAAGACGCCACGCGAGGACATGTACGCTCGCGAGCATAAGACGGCGTCCCCGCCTACATGCTGCTTCGCACATCGATATCTATTCGTCATAATGTAGTACTTATGGCCCATGGTACGCTGCGACTGGGGCATCTATTGAAGGGAATATACGCGAATTAATCATAACTGAACGACCCACTCCACTAGCCGGCTGCCGCCGAGCGGCGTGACCACTGCTTATCTATCCGCATCGTTGCTACCCTATTATTGGATCGATAATATACCCTGTACGTTACTACGTCGCAGCCTTATTCAATGAATCAATACTAGACCACGACGTCGGTACCAGCTGCTCGAAGGTACTATAACCAAGCAGCTGACCAGATTTTCTGGCCCACATTAATTCTTAACATAAACACGTGTCACAAGGCCTTCTGCATACCACGGCTGAAGCCTCATTTATCGTTGGCTGGGATCGTGAGGTGCCACCCGTTACTGAAACTACACCCTTCTAAATGAACATACAATTTCGATTATAACCACAGCTCACACAATAGTTTGACGGCCCATGCATGGGCTCCTTCTCTCGTCTGAAACTCAAAGCTTAAAATCGCTCCCGTTTTAGTGACAACGTACCTCATACT"
    d = 4

    print(" ".join(approximatePatternMatching(pattern, genome, d)))


if __name__ == '__main__':
    main()