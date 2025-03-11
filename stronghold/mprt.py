#!/usr/bin/env python

# https://rosalind.info/problems/mprt/

# get fasta for this file with mprt.sh

from parsefasta import parse_fasta
import argparse
import re

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--fasta", help="Input fasta file path", type=str, required=True) 
    parser.add_argument("-i", "--input", help="Input accestion Ids.", type=str, required=True) 
    return parser.parse_args()

# The asparagine-X-serine/threonine (NXS/T) motif, 
# where X is any amino acid except proline, 
# is the consensus motif for N-linked glycosylation. 
#
# Lam PV, Goldman R, Karagiannis K, Narsule T, Simonyan V, Soika V, Mazumder R. Structure-based comparative analysis and prediction of N-linked glycosylation sites in evolutionarily distant eukaryotes. Genomics Proteomics Bioinformatics. 2013 Apr;11(2):96-104. doi: 10.1016/j.gpb.2012.11.003. Epub 2013 Feb 28. PMID: 23459159; PMCID: PMC3914773.
MOTIF = "N[^P][ST]"
MOTIF_LEN = 3

def text_from_list(filepath: str) -> list:
    my_list = []
    with open(filepath, 'r') as fin:
        for line in fin:
            my_list.append(str(line.strip()))
    return my_list

def main():
    sequences = parse_fasta(get_args().fasta)
    ids = text_from_list(get_args().input)
    # I assume that sequences and ids are in the same order
    
    if len(sequences) != len(ids):
        raise RuntimeError("sequences and ids not the same length")

    for index, sequence in enumerate(sequences):
        locations = []
        print(ids[index]) 

        for match in re.finditer(rf"(?=({MOTIF}))", sequence.seq): 
            print(match.start() + 1, end = " ")
        print()

if __name__ == "__main__":
    main()
