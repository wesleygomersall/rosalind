#!/usr/bin/env python

# https://rosalind.info/problems/prob/

import argparse
import math

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for i, line in enumerate(fin): 
        if i == 0: seq = line.strip()
        if i == 1: arr = line.split()

b_arr = []

for gc in arr: 
    g = c = 0.5 * float(gc)
    a = t = 0.5 * (1 - float(gc)) 

    prob = 1
    for base in seq: 
        match base: 
            case "A": prob = prob * a 
            case "T": prob = prob * t 
            case "C": prob = prob * c 
            case "G": prob = prob * g 

    b_arr.append(math.log(prob, 10))

for index, p in enumerate(b_arr): 
    if index == len(b_arr) - 1: print(f"{p:.{3}f}") 
    else: print(f"{p:.{3}f}", end=' ') 
