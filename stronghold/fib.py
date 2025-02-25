#!/usr/bin/env python

# https://rosalind.info/problems/fib/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for line in fin: 
        nk = line.split()

n = int(nk[0]) # months (n <= 40) 
k = int(nk[1]) # rabbit pairs per generation (k <= 5) 

start = 1 # start with 1 pair of rabbits

for month in range(n): 
    if month < 1: # rabbits take 2 months to mature
        two_ago = 0 
        one_ago = 0 
        new = 0
        total = start
    else: 
        two_ago = one_ago
        one_ago = total
        new = two_ago * k 
        total = new + one_ago 

print(total) 
