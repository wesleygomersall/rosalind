#!/usr/bin/env python 

# https://rosalind.info/problems/iev/

# Given: Six nonnegative integers, each of which does not exceed 20,000. 
#           The integers correspond to the number of couples in a population 
#           possessing each genotype pairing for a given factor. 
#           In order, the six given integers represent the number of couples having the following genotypes:
#           1. AA-AA
#           2. AA-Aa
#           3. AA-aa
#           4. Aa-Aa
#           5. Aa-aa
#           6. aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
#           under the assumption that every couple has exactly two offspring.
# 
# Sample input: 1 0 0 1 0 1
# Sample output: 3.5

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

args.input

with open(args.input) as fin: 
    for line in fin: 
        inputs = line.split()

num1 = int(inputs[0])
num2 = int(inputs[1])
num3 = int(inputs[2])
num4 = int(inputs[3])
num5 = int(inputs[4])
num6 = int(inputs[5])

off1 = num1 * 1 * 2
off2 = num2 * 1 * 2
off3 = num3 * 1 * 2
off4 = num4 * 0.75 * 2
off5 = num5 * 0.5 * 2
off6 = num6 * 0 * 2

expected = off1 + off2 + off3 + off4 + off5 + off6

print(expected) 
