#!/usr/bin/env python

# https://rosalind.info/problems/spec/

import argparse

def protein_prefix_spectrum(masses: list) -> str: 
    aa = []
    for i in range(len(masses)):
        if i == len(masses) - 1: break
        diff = float(masses[i + 1]) - float(masses[i])
        nearest_aa = ""
        closest = 1000000
        for key in MONOISOTOPIC_MASS:

            if closest > (float(MONOISOTOPIC_MASS[key]) - diff) ** 2:
                closest = (float(MONOISOTOPIC_MASS[key]) - diff) ** 2
                closest_aa = key
        aa.append(closest_aa)
                
    return aa

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

def main(args):
    values = []
    with open(args.input, 'r') as fin:
        for line in fin:
            values.append(float(line.strip()))

    protein = protein_prefix_spectrum(values)

    for aa in protein: 
        print(aa, end="")
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", type=str, required=True) 
    args = parser.parse_args()
    main(args)
