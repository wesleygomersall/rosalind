#!/usr/bin/env python

# https://rosalind.info/problems/cons/

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file name", type=str, required=True) 
    return parser.parse_args()

args = get_args()

sequence = ""
first_entry = True

with open(args.input, 'r') as fin: 
    for line_num, line in enumerate(fin): 
        if line.startswith('>') and not line_num == 0:
            if first_entry: 
                a = [0] * len(sequence)
                c = [0] * len(sequence)
                g = [0] * len(sequence)
                t = [0] * len(sequence)
                first_entry = False
            for i in range(len(sequence)):
                match sequence[i]:
                    case "A":
                        a[i] += 1
                    case "C":
                        c[i] += 1
                    case "G":
                        g[i] += 1
                    case "T":
                        t[i] += 1
            sequence = ""
        if not line.startswith('>'):
            sequence = sequence + line.strip()
    for i in range(len(sequence)):
        match sequence[i]:
            case "A":
                a[i] += 1
            case "C":
                c[i] += 1
            case "G":
                g[i] += 1
            case "T":
                t[i] += 1

consensus = ""
for i in range(len(a)):
    if max(a[i], c[i], g[i], t[i]) == a[i]: consensus = consensus + "A"
    elif max(a[i], c[i], g[i], t[i]) == c[i]: consensus = consensus + "C"
    elif max(a[i], c[i], g[i], t[i]) == g[i]: consensus = consensus + "G"
    elif max(a[i], c[i], g[i], t[i]) == t[i]: consensus = consensus + "T"
print(consensus)

print("A:", end="")
for i in range(len(a)): print(f" {a[i]}", end="")
print("\nC:", end="")
for i in range(len(c)): print(f" {c[i]}", end="")
print("\nG:", end="")
for i in range(len(g)): print(f" {g[i]}", end="")
print("\nT:", end="")
for i in range(len(t)): print(f" {t[i]}", end="")
print()
