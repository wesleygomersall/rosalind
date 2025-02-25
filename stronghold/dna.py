#!/usr/bin/env python

# https://rosalind.info/problems/dna/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for line in fin: 
        seq = line

a = 0; c = 0; g = 0; t = 0

for base in seq: 
    match base: 
        case "A":
            a += 1
        case "C":
            c += 1
        case "G":
            g += 1
        case "T":
            t += 1

print(f"{a} {c} {g} {t}")
