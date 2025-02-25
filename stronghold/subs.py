#!/usr/bin/env python

# https://rosalind.info/problems/prot/

import argparse
import re

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for i, line in enumerate(fin): 
        if i == 0: seq = line.strip()
        if i == 1: motif = line.strip()


locations = []
# use lookahead to get overlapping matches, loop through matches
for match in re.finditer(rf"(?=({motif}))", seq): 
    locations.append(match.start() + 1)

for i, index in enumerate(locations): 
    if i == len(locations) - 1: print(index)
    else: print(index, end= " ")
