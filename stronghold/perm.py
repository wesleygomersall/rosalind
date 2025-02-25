#!/usr/bin/env python

# https://rosalind.info/problems/perm/
# for a given n <= 7, return the total number of permutations,
# followed by a list of all possible permutations, space separated. 

import argparse
import math
import random

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for line in fin: 
        n = int(line.strip()) 

num_perms = math.factorial(n)

perms = set()

for i in range(num_perms): 
    while True: 
        attempt: list = random.sample(range(1, n + 1), n)
        s = "" 
        for a in attempt: s = s + " " + str(a) 
        s = s.lstrip()
        if s not in perms: break
    perms.add(s)

print(num_perms) 
for p in perms: 
    print(p) 
