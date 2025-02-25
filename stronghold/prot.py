#!/usr/bin/env python

# https://rosalind.info/problems/prot/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

CODON_TABLE = {
        "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
        "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
        "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
        "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
        "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
        "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
        "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
        "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
        "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
        "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
        "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
        "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
        "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
        "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
        "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
        "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}

with open(args.input, 'r') as fin: 
    for line in fin: 
        seq = line.strip()

prot = "" 
index = 0 

# for i in range(len(seq) / 3): 
while True:
    if index == len(seq): break
    codon = seq[index] + seq[index + 1] + seq[index + 2] 
    if CODON_TABLE[codon] == "Stop": break
    prot = prot + CODON_TABLE[codon]
    index += 3

print(prot) 
