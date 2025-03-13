#!/usr/bin/env python

# https://rosalind.info/problems/full/

import argparse

MONOISOTOPIC_MASS = {"A": "71.03711", "C": "103.00919",
                     "D": "115.02694", "E": "129.04259",
                     "F": "147.06841", "G": "57.02146",
                     "H": "137.05891", "I": "113.08406",
                     "K": "128.09496", "L": "113.08406",
                     "M": "131.04049", "N": "114.04293",
                     "P": "97.05276", "Q": "128.05858",
                     "R": "156.10111", "S": "87.03203",
                     "T": "101.04768", "V": "99.06841",
                     "W": "186.07931", "Y": "163.06333 "}

def pair_element_sum(full: float, some_list: list) -> list:
    '''For some float value given by `full` and a list of float values
    given in `some_list`, pairs the elements of the list which roughly 
    sum to `full`.
    Return a set of frozen sets which each contain a pair from `some_list`.
    '''

    b_y_paired = set()
    for i, j in enumerate(some_list):
        for k, l in enumerate(some_list):
            if i == k: continue
            diff = some_list[i] - some_list[k]
            if round(some_list[i] + some_list[k], 2) == round(full, 2):
                b_y_paired.add(frozenset([some_list[i], some_list[k]]))
    return b_y_paired

def closest_monoisotipic_mass(some_mass: float) -> str:
    '''Rounds monoisotipic masses and some_mass to nearest 0.01.
    If a match is found between any known mass and the input, 
    returns the 1-letter code for the amino acid.
    '''

    for m in MONOISOTOPIC_MASS.keys():
        if round(float(MONOISOTOPIC_MASS[m]), 2) == round(some_mass, 2):
    return amino_acid 

def main(args):
    masses = []
    with open(args.input, 'r') as fin:
        for line in fin:
            masses.append(float(line.strip()))

    full_mass = masses.pop(0)
    peptide_len = len(masses) / 2 - 1
    print(peptide_len)
    print(full_mass)
    print(masses)
    pairs = pair_element_sum(full_mass, masses)
    print(len(pairs))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", type=str, required=True) 
    args = parser.parse_args()
    main(args)
