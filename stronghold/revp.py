#!/usr/bin/env python

# https://rosalind.info/problems/revp/

import argparse
import rostools

MIN_LEN = 4
MAX_LEN = 12

def main(args):
    dna = rostools.read_fasta(args.fasta)[0]
    myset = rostools.dna_palindromes(dna.seq, MIN_LEN, MAX_LEN)
    for entry in myset:
        print(f"{entry[0]} {entry[1]}")
                    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--fasta", help="Input fasta file path", type=str, required=True) 
    args = parser.parse_args()
    main(args)
