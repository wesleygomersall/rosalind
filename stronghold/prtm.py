#!/usr/bin/env python

# https://rosalind.info/problems/prtm/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", 
                        type=str, required=True) 
    return parser.parse_args()

args = get_args()

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

protein = ""

if __name__ == "__main__":
    with open(args.input, 'r') as fin: 
        for line in fin: 
            protein = protein + line.strip()

    weight = 0

    for aa in protein:
        if aa not in MONOISOTOPIC_MASS.keys():
            print("error")
        else:
            weight += float(MONOISOTOPIC_MASS[aa])

    print(f"{weight:.{3}f}")

