#!/usr/bin/env python

# https://rosalind.info/problems/tran/

import argparse
import rostools

def compare_dna(sequence1: str, sequence2: str) -> dict:
    mut_counts = dict()
    assert len(sequence1) == len(sequence2)
    
    mutations = [(sequence1[i], sequence2[i]) for i in range(len(sequence1))]

    # create counts dictionary: keys are each type of mutation
    for base_tuple in set(mutations):
        if base_tuple[0] == base_tuple[1]: 
            mut_counts["Identity"] = 0
        else:
            mut_counts[base_tuple[0] + base_tuple[1]] = 0

    # loop through mutations and tally in mut_counts
    for base_tuple in mutations: 
        if base_tuple[0] == base_tuple[1]: 
            mut_counts["Identity"] += 1
        else:
            mut_counts[base_tuple[0] + base_tuple[1]] += 1

    return mut_counts

def main(args):
    tran_seqs = rostools.read_fasta(args.input)
    transitions = 0
    transversions = 0

    mutation_count = compare_dna(tran_seqs[0].seq, tran_seqs[1].seq)

    for key, value in mutation_count.items(): 
        match key: 
            # transitions are purine-purine or pyrimidine-pyrimidine
            case "AG" | "GA": transitions += value
            case "TC" | "CT": transitions += value
            # transitions are purine-pyrimidine exchange
            case "AT" | "TA": transversions += value
            case "AC" | "CA": transversions += value
            case "CG" | "GC": transversions += value
            case "TG" | "GT": transversions += value

    if transversions > 0:
        print(f"{transitions/transversions:.11f}")
    else: 
        print(0)

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", 
                        type=str, required=True) 
    args = parser.parse_args()
    main(args)
