#!/usr/bin/env python

# https://rosalind.info/problems/full/

import argparse

MONOISOTOPIC_MASS = {"A": 71.03711, "C": 103.00919,
                     "D": 115.02694, "E": 129.04259,
                     "F": 147.06841, "G": 57.02146,
                     "H": 137.05891, "I": 113.08406,
                     "K": 128.09496, "L": 113.08406,
                     "M": 131.04049, "N": 114.04293,
                     "P": 97.05276, "Q": 128.05858,
                     "R": 156.10111, "S": 87.03203,
                     "T": 101.04768, "V": 99.06841,
                     "W": 186.07931, "Y": 163.06333}

def closest_monoisotipic_mass(some_mass: float) -> str:
    '''Rounds monoisotipic masses and some_mass to nearest 0.01.
    If a match is found between any known mass and the input, 
    returns the 1-letter code for the amino acid.
    '''

    for aa in MONOISOTOPIC_MASS.keys():
        if round(float(MONOISOTOPIC_MASS[aa]), 2) == round(some_mass, 2):
            return aa 
    return ""

def probable_prot(parent_mass: float, betagammas: list) -> str:
    n = int(len(betagammas) / 2 - 1) # peptide length n 
    prot: str = ""
    coordinates = []
    bgmasses = betagammas.copy()
    bgmasses.sort() # arrange complementary values to [0] and [-1]

    w1 = min(bgmasses) # w1 add to peptide prefix mass
    w2: float = 0.0 # w2 add to peptide suffix mass

    w1 = bgmasses.pop(0)
    bion_mass = w1
    yion_mass = bgmasses.pop(-1)
    coordinates.append((bion_mass, yion_mass)) # first bion-yion pair

    for aanumber in range(n):
        index1 = 0
        index2 = 0
        for m in bgmasses:
            if m < bion_mass: continue
            possible_aa = closest_monoisotipic_mass(abs(bion_mass - m))
            if possible_aa != "":
                prot = prot + possible_aa
                bion_mass = m
                break
            else: index1 += 1

        for n in bgmasses:
            if round(parent_mass, 2) == round(n + bion_mass, 2): 
                yion_mass = n
                break
            else: index2 += 1

    return prot

def main(args):
    masses = []
    with open(args.input, 'r') as fin:
        for line in fin:
            masses.append(float(line.strip()))
    full_mass = masses.pop(0)
    print(probable_prot(full_mass, masses))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", 
                        type=str, required=True) 
    args = parser.parse_args()
    main(args)
