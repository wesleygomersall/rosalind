#!/usr/bin/env python

# https://rosalind.info/problems/sseq/

import argparse
import rostools

def subsequence(s:str, t: str) -> list:
    '''Returns the indices of sequence `s` (1-based) 
    of first encountered subsequence `t` in `s`.
    A subsequence of s is a string si1, si2, ..., sik, where 1≤i1<i2⋯<ik≤n.
    '''
    j = 0
    indices = []
    for i, char in enumerate(s):
        if char == t[j]:
            indices.append(i + 1)
            j += 1
            if j == len(t): break
    return indices

def print_spaced_list(some_list: list):
    '''Prints the elements of a list out to a single line.
    Elements are separated by a single space with no space at either end.
    '''
    list_copy = some_list.copy()
    print(list_copy.pop(0), end="")
    [print(f" {i}", end='') for i in list_copy]
    print()

def main(args):
    my_dnas = rostools.read_fasta(args.input)
    subseq = subsequence(my_dnas[0].seq, my_dnas[1].seq)
    spaced_list(subseq)
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", help="Input file path", 
                        type=str, required=True) 
    args = parser.parse_args()
    main(args)
