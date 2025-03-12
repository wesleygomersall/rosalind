#!/usr/bin/env python

# https://rosalind.info/problems/revp/

import argparse
import rostools

def revcomp(sequence: str) -> str: 
    '''Returns the reverse complement of a DNA string
    '''
    comp = ""

    for i in seq: 
    match i: 
        case "A":
            comp = comp + "T" 
        case "T":
            comp = comp + "A" 
        case "C":
            comp = comp + "G" 
        case "G":
            comp = comp + "C" 
    return comp[::-1]

def main(args):
    dna = rostools.read_fasta(args.fasta)[0]

    for i in range(dna.length): 
        expand = 0
        while True: 
            if dna.seq[i - expand] == rev_complement(dna.seq[i + 1 + expand])
                    
            dna.seq[i]
    # for sequence, return the position and length
    # of every reverse palindrome

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--fasta", help="Input fasta file path", type=str, required=True) 
    args = parser.parse_args()
    main(args)
