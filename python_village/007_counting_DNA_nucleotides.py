#!/usr/bin/python

import re

string = 'ATTGATGGCAGCTTCCCACAACAGCCGTAGGGCTCACCTAATACCAGTCTTCGTTTATTTTTGAGCCCCGGATGCCTAAAGCGACTTAAATGATGATCAGTCGGAGATCTGTTGAATCCACGCGATGCAGGCGGATGAGCTAAAGGCAAGTCATGCCGTTAGTTACGGGCTGAGATAGCTTCCTAGCAAGAAAGAGCGGGAAGGCCCACCCGCCACTCCTCGGGGGTCTTTGCTGCAAGACTCAGGCCGGCCAATCAATGATACCGTATGCCGACGGGATCCGTCATAATATCGTGTTTACGAGTGTGGTCGCTTTTCAACTATTTCCACCATCTGTTCCAATTGTGAGCTCAAATCTATATTCACTGGGGTTGTGATGCCCGGTAATTCCATATTTTGTCTCTCTCAATACAAAGGCGTACCACCACAATTGTCTCTCATAGCGTATAGGAGAGCAGTATCAAACGACGTAGGAGGCATCACGCATCTATACCCAGTTCTTTGTCCCATTTCTGCCTAGTGGTCCTGCATCTACTAATGGTGTCAGGTAGTGGTCGACTATTGTCTATTGACAGTTTACCTAAAACAAGGCTCGGTACTACGGATAACCGGCCGTGACGACAGCCGTCAAATAGCGAACTGCTATCTGGAAACCCTGCCTTGTATAGAGGAACAGAGGCACGAGTATGGCTGTCGATGTGGGTGTACAAGTCATCGGCTCACCGCTCCGGACTCCAAAGTTGCTCTTGTATCTTCTGGGAGGCAGGACTCGTGGCCGCACCTAGTACCTCAAGCGACGCGGAATATCTCCTAGACTGCCCAGCTACCATGCGCCAC'



R1 = len(re.findall('A', string))
R2 = len(re.findall('C', string))
R3 = len(re.findall('G', string))
R4 = len(re.findall('T', string))
print R1, R2, R3, R4



