#!/usr/bin/env python

# https://rosalind.info/problems/hamm/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for i, line in enumerate(fin): 
        if i == 0: s = line.strip()
        if i == 1: t = line.strip()

assert len(s) == len(t)

count = 0 

for index in range(len(s)): 
    if s[index] == t[index]: continue
    else: count += 1

print(count) 
