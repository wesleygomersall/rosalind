#!/usr/bin/env python

# https://rosalind.info/problems/grph/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

K = 3 # problem asks for O3

class FastaRec:
    def __init__(self, header, sequence):
        self.head = header.strip('>')
        self.seq = sequence
        self.len = len(sequence)

    def left_k(self, another, k):
        if self.seq == another.seq: pass
        elif self.seq[(self.len-k) : self.len] == another.seq[0:k]: 
            return f"{self.head} {another.head}"

def adjacency(sequences: list, k): 
    adj = set()
    for record in sequences: 
        for second_record in sequences: 
            left = record.left_k(second_record, k)
            if left is not None: adj.add(left)
    for edge in adj: 
        print(edge)

sequences: list = []

with open(args.input, 'r') as fin: 
    for linenum, line in enumerate(fin): 
        if line.startswith('>'): 
            if linenum != 0: 
                newseq = FastaRec(name, seq)
                sequences.append(newseq) 
            name = line.strip()
            seq = "" 
        else: 
            seq = seq + line.strip()

adjacency(sequences, K)
