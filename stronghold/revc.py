#!/usr/bin/env python 

# https://rosalind.info/problems/revc/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for line in fin:
        seq = line

rc = ""

for i in seq: 
    match i: 
        case "A":
            rc = "T" + rc
        case "T":
            rc = "A" + rc
        case "C":
            rc = "G" + rc
        case "G":
            rc = "C" + rc

print(rc) 

