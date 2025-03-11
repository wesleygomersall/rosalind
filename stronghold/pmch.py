#!/usr/bin/env python

# https://rosalind.info/problems/pmch/

import argparse
import math

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", 
                        type=str, required=True) 
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    sequence: str = ""

    with open(args.input, 'r') as fin: 
        for linenum, line in enumerate(fin): 
            if line.startswith('>'): 
                # name = line.strip()
                continue
            sequence = sequence + line.strip()

    a = 0
    c = 0
    matches = 1

    for b in sequence:
        match b:
            case "A":
                a += 1
            case "C":
                c += 1
            case _:
                continue

    matches = matches * math.factorial(a) * math.factorial(c)
    print(matches)
