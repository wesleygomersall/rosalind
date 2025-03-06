#!/usr/bin/env python

# https://rosalind.info/problems/fibd/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for line in fin: 
        nm = line.split()

n = int(nm[0]) # nth month (n <= 100)
m = int(nm[1]) # after m months (m <= 20) 
# return the number of pairs of rabbits after the nth month if all rabbits live m months

start = 1 # start with 1 pair of rabbits

newbunnies = [start]
for month in range(n): 

    if month >= m: 
        total -= newbunnies[month - m]

    if month < 1: # rabbits take 1 month to mature
        two_ago = 0 
        one_ago = 0 
        new = 0
        total = start

    else: 
        two_ago = one_ago
        one_ago = total
        new = two_ago 
        total += new  
        newbunnies.append(new) 

print(total) 
