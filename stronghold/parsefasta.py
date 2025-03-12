#!/usr/bin/env python

'''
Parse Fasta by Wesley Gomersall, 2025-03-10

For reading fasta sequences and storing them into memory.

Import this module to another script in this dir.
Add the following to script:

    sequences = parsefasta.parse_fasta(parsefasta.get_args().input)

The returned `sequences` is a list of FastaRec objects.
'''

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path(s)", type=str, required=True) 
    return parser.parse_args()

class FastaRec:
    '''
    A fasta record with a name and a sequence and a length

    Attributes:
        head (str):         Fasta header (with '>' removed.
        seq (str):          Fasta sequence.
        len (int):          Length of fasta sequence.

    Method(s):
        none
    '''

    def __init__(self, header, sequence):
        self.head = header.strip('>')
        self.seq = sequence
        self.len = len(sequence)

def parse_fasta(filepath: str) -> list:
    '''Create list of motifs (entries class Motif).

    Input(s):
        filepath (str):     File path of input fasta file.

    Output(s):
        list:               List of FastaRec objects.
    '''

    sequences = []

    with open(filepath, 'r') as fin: 
        for linenum, line in enumerate(fin): 

            if line.startswith('>'): 
                if linenum != 0: 
                    newseq = FastaRec(name, seq)
                    sequences.append(newseq) 
                name = line.strip()
                seq = "" 

            else: 
                seq = seq + line.strip()

        newseq = FastaRec(name, seq)
        sequences.append(newseq) 

    return sequences

if __name__ == "__main__":

    args = get_args()

    sequences = parse_fasta(args.input)

    print(f"Imported fasta: {args.input}")
    for i, sequence in enumerate(sequences):
        print(f"\nEntry {i}:")
        print(f">{sequence.head}")
        print(sequence.seq)
