#!/usr/bin/env python

import parsefasta as pf
# from rostools import DNA_CODONS
import rostools as rt

def main(args):
    sequences = pf.parse_fasta(args.input)

    dna = sequences.pop(0).seq

    for intron in sequences: 
        dna = rt.remove_substring(dna, intron.seq) 

    print(rt.translate(dna))

if __name__ == "__main__":
    main(pf.get_args())

