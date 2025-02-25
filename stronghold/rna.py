#!/usr/bin/env python

# https://rosalind.info/problems/rna/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for line in fin: 
        seq = line.strip()

rna = "" 

for base in seq: 
    if base == "T":
        rna = rna + "U"
    else: 
        rna = rna + base
        
print(rna)
