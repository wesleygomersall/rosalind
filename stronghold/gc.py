#!/usr/bin/env python 

# https://rosalind.info/problems/gc/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

def gc_content(sequence): 
    counter = 0
    for base in sequence: 
        if base == 'C' or base == 'G': 
            counter += 1
    if len(sequence) == 0: return 0
    else:
        gc = counter / len(sequence) * 100
        return gc

FASTA = args.input

seq_ID = ""
seq_gc = 0
largest_ID = ""
largest_gc = 0
seq = "" 

with open(FASTA, 'r') as fasta: 
    for line in fasta: 
        if line.startswith('>'): 
            
            seq = "" 
            seq_gc = gc_content(seq.strip()) 

            if seq_gc > largest_gc: 
                largest_ID = seq_ID
                largest_gc = seq_gc

            seq_ID = line.strip('>').strip()
        else: 
            seq = seq + line.strip()

    seq_gc = gc_content(seq.strip()) 
    if seq_gc > largest_gc: 
        largest_ID = seq_ID
        largest_gc = seq_gc

print(largest_ID)
print(round(largest_gc, 6))
