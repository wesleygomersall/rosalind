#!/usr/bin/env python

# https://rosalind.info/problems/lexf/

import argparse
import numpy as np
import rostools

def main(args):
    with open(args.input, 'r') as fin:
        for line_num, line in enumerate(fin):
            if line_num == 0: alphabet = line.split()
            if line_num == 1: length = int(line.strip())
    
    # Alphabet is a list already in alphabetical order. 
    
    mylist = []
    dexlist = []

    for i in range(len(alphabet) ** length):
        temp = ""
        dex = ""
        for n in range(length):
            if n == 0: 
                index = i % len(alphabet)
            else: 
                index = i // (len(alphabet) ** n) % len(alphabet)
            dex = str(index) + dex
            temp = alphabet[index] + temp
        mylist.append(temp)
        dexlist.append(dex)

    for l in mylist: 
        print(l)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", type=str, required=True) 
    args = parser.parse_args()
    main(args)
