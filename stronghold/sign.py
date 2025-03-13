#!/usr/bin/env python

# https://rosalind.info/problems/sign/

import argparse
from itertools import permutations
from itertools import combinations

def main(args):
    with open(args.input, 'r') as fin:
        for line_num, line in enumerate(fin):
            if line_num == 0: 
                n = int(line.strip())
    
    sig_perm = signed_permutation(n)
    print(len(sig_perm))
    for item in sig_perm:
        for i in range(n):
            if i == n - 1: # last item gets \n
                print(int(item[i]))
            else:
                print(int(item[i]), end= " ")

def signed_permutation(n: int) -> set:
    myset = set()
    values = [i + 1 for i in range(n)]
    signs = [int(2 * ((i % 2) - 0.5)) for i in range(2 * int(n))] 
    sign_combos = set(combinations(signs, n))

    for perm in permutations(values):
        for combo in sign_combos:
            assert len(combo) == len(perm)
            temp = []
            for i in range(len(perm)):
                temp.append(perm[i] * combo[i])
            myset.add(tuple(temp))

    return myset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", 
                        type=str, required=True) 
    args = parser.parse_args()
    main(args)
