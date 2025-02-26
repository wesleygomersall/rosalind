#!/usr/bin/env python

# https://rosalind.info/problems/prob/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

with open(args.input, 'r') as fin: 
    for i, line in enumerate(fin): 
        if i == 0: seq = line.strip()
        if i == 1: arr = line.split()

