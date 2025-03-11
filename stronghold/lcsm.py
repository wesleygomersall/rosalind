#!/usr/bin/env python

# https://rosalind.info/problems/lcsm/

import parsefasta

def longest_substring(string1: str, string2: str) -> set:
    '''Finds longest common substring between two strings.

    Input(s):
        string1 (str):      First string.
        string2 (str):      Second string.

    Output(s):
        set:                Longest common substring between a and b.
    '''

    mystrings = set()
    longest_string = 0
    arr = [[0 for j in range(len(string2))] for i in range(len(string1))]

    for i in range(len(string1)):
        for j in range(len(string2)):

            if string1[i] == string2[j]: 
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1] + 1
            
                if arr[i][j] > longest_string:
                    longest_string = arr[i][j]
                    print(f" longest string found so far in common is {longest_string - 1}")
                    print(string1[(i - longest_string + 1):i])
                    mystrings = set(string1[(i - longest_string + 1):i])
                elif arr[i][j] == longest_string:
                    mystrings.add(string1[(i - longest_string + 1):i])
            else:
                arr[i][j] = 0

    return arr
    # return mystrings

def main():
    sequences = parsefasta.parse_fasta(parsefasta.get_args().input)
    
    for s in sequences:
        for s2 in sequences:
            if s.head == s2.head: continue
            else:
                print()
                print(s.seq)
                print(s2.seq)
                substrings = longest_substring(s.seq, s2.seq)
                print(substrings)

    
if __name__ == "__main__":
    main()
