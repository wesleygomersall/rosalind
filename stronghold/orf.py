#!/usr/bin/env python

# https://rosalind.info/problems/orf/

import argparse
import rostools

def translate_all(sequence: str) -> list:
    '''Translate DNA nuc_acid.
    Sequence must have at least one start codon to find the reading frame(s).
    Translates each protein until the first stop codon encountered.
    '''
    # to begin: empty protein str and not translating
    length_of_sequence = len(sequence)
    protein: str = ""
    proteins: list = []
    translating: bool = False
    i = 0

    while True:
        if i + 3 >= length_of_sequence:break 

        # print(sequence[i:i+3])
        if not translating:
            if sequence[i:i+3] == "ATG":
                translating = True
                prot_start = i
                protein = protein + "M"
                i += 3
            else: i += 1
        elif translating:
            if rostools.DNA_CODONS[sequence[i:i+3]] == "Stop":
                translating = False
                proteins.append(protein) 
                protein = "" 
                i = prot_start + 1
            else: 
                protein = protein + rostools.DNA_CODONS[sequence[i:i+3]]
                i += 3

    return proteins

def main(args):
    my_dna = rostools.read_fasta(args.input)[0]

    protset = set(translate_all(my_dna.seq))
    protset = protset.union(set(translate_all(rostools.revcomp(my_dna.seq))))

    [print(i) for i in protset]

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", 
                        type=str, required=True) 
    args = parser.parse_args()
    main(args)
