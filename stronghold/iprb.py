#!/usr/bin/env python 

# https://rosalind.info/problems/iprb/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

args.input

with open(args.input) as fin: 
    for line in fin: 
        kmn = line.split()

k = int(kmn[0]) # num homozygous dominant
m = int(kmn[1]) # num heterozygotes
n = int(kmn[2]) # num homozygous recessive
total = (k + m + n)

# Return: The probability that two randomly selected mating organisms 
#           will produce an individual possessing a dominant allele 
#           (and thus displaying the dominant phenotype). 
#           Assume that any two organisms can mate.
# Sample input: 2 2 2 
# Sample output: 0.78333

# case 1: 
    # at least one k -> guaranteed
c1 = (k / total) * 1
# case 2: 
    # at least one m -> if k: 1, if m: 0.75, if n: 0.5
c2 = (m / total) * (((k / (total - 1)) * 1) + (((m-1) / (total - 1)) * 0.75) + ((n / (total - 1)) * 0.5))
# case 3: 
    # at least one n -> if k: 1, if m: 0.5, if n: 0
c3 = (n / total) * (((k / (total -1 )) * 1) + ((m / (total - 1)) * 0.5) + (((n-1) / (total - 1)) * 0))

prob = c1 + c2 + c3
print(round(prob, 5))
