#!/usr/bin/env python

# https://rosalind.info/problems/revp/

import argparse
import rostools

def main(args):
    sequence = rostools.read_fasta(args.fasta)[0]

    # for sequence, return the position and length
    # of every reverse palindrome

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--fasta", help="Input fasta file path", type=str, required=True) 
    args = parser.parse_args()
    main(args)
