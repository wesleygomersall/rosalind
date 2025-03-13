#!/usr/bin/env python

def remove_substring(string: str, sub: str) -> str:
    '''Removes substring `sub` from `string` and returns shortened string. 
    If `sub` not found, return `string` unchanged. 
    '''
    string_len = len(string)
    sub_len = len(sub)
    for i in range(string_len - sub_len + 1):
        if (string[i: i + sub_len] == sub): 
            return string[0:i] + string[i + sub_len : string_len]
    return string

def translate(nuc_acids: str, dna: bool = True) -> str:
    '''Translate nucleic acid sequence (default DNA) to protein.
    This function is currently ignorant of reading frame
    '''
    if dna: codon_table = DNA_CODONS
    else: codon_table = RNA_CODONS

    prot = "" 
    index = 0 

    while True:
        if index > len(nuc_acids) - 3: break

        codon = nuc_acids[index] + nuc_acids[index + 1] + nuc_acids[index + 2] 

        if codon_table[codon] == "Stop": break
        prot = prot + codon_table[codon]
        index += 3

    return prot

class BioSequence:
    '''
    A biological record with a name and a sequence

    Attributes:
        id (str):           Sequence ID
        seq (str):          Sequence

    Method(s):
        length (int):       Returns the length of `seq`
    '''

    def __init__(self, header: str, sequence: str):
        self.id = header.strip('>')
        self.seq = sequence
    
    @property
    def length(self) -> int: 
        return len(self.seq) 

def read_fasta(filepath: str) -> list:
    '''Create list of motifs (entries class Motif).

    Input(s):
        filepath (str):     File path of input fasta file.

    Output(s):
        list:               List of BioSequence objects.
    '''

    sequences = []

    with open(filepath, 'r') as fin: 
        for linenum, line in enumerate(fin): 

            if line.startswith('>'): 
                if linenum != 0: 
                    newseq = BioSequence(name, seq)
                    sequences.append(newseq) 
                name = line.strip()
                seq = "" 

            else: 
                seq = seq + line.strip()

        newseq = BioSequence(name, seq)
        sequences.append(newseq) 

    return sequences

def revcomp(sequence: str, dna: bool = True) -> str: 
    '''Returns the reverse complement of a DNA string by default.
    '''
    compstrand = ""

    if dna: complement = DNA_COMP_BASES
    else: complement = RNA_COMP_BASES

    for i in sequence:
        compstrand = compstrand + complement[i]

    # for i in sequence: 
        # match i: 
            # # case "A":
                # comp = comp + "T" 
            # case "T":
                # comp = comp + "A" 
            # # case "C":
                # comp = comp + "G" 
            # case "G":
                # comp = comp + "C" 
    return compstrand[::-1]

def dna_palindromes(sequence: str, minimum: int, maximum: int) -> set:
    '''Return a set of tuples containing all reverse palindromes found in 
    DNA sequence that are `minimum` <= length <= `maximum`.

    Each tuple in list is: 
    (reverse palindrome location (1-based index), 
     reverse palindrome length)
    '''
    revpals = set()
    for i in range(len(sequence)): 
        expand = 0
        pal_length = 0

        while True: 
            if i - expand < 0 or i + 1 + expand > len(sequence): 
                if minimum <= pal_length and pal_length <= maximum:
                    revpals.add((i - expand + 2, pal_length))
                break
            left = sequence[i - expand:i+1] 
            right = sequence[i + 1: i + 2 + expand]
            right_rc = revcomp(right, True)
            if left == right_rc:
                pal_length = len(left + right)
                expand += 1
                if minimum <= pal_length and pal_length <= maximum:
                    revpals.add((i - expand + 2, pal_length))
            else: 
                break
    return revpals

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

DNA_CODONS = {"TTT": "F",      "CTT": "L",      "ATT": "I",      "GTT": "V",
              "TTC": "F",      "CTC": "L",      "ATC": "I",      "GTC": "V",
              "TTA": "L",      "CTA": "L",      "ATA": "I",      "GTA": "V",
              "TTG": "L",      "CTG": "L",      "ATG": "M",      "GTG": "V",
              "TCT": "S",      "CCT": "P",      "ACT": "T",      "GCT": "A",
              "TCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
              "TCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
              "TCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
              "TAT": "Y",      "CAT": "H",      "AAT": "N",      "GAT": "D",
              "TAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
              "TAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
              "TAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
              "TGT": "C",      "CGT": "R",      "AGT": "S",      "GGT": "G",
              "TGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
              "TGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
              "TGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}

RNA_CODONS = {"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
              "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
              "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
              "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
              "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
              "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
              "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
              "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
              "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
              "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
              "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
              "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
              "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
              "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
              "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
              "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}

DNA_COMP_BASES = {"A": "T", "a": "t", 
                  "T": "A", "t": "a",
                  "C": "G", "c": "g",
                  "G": "C", "g": "c"}

RNA_COMP_BASES = {"A": "U", "a": "u", 
                  "U": "A", "u": "a",
                  "C": "G", "c": "g",
                  "G": "C", "g": "c"}

if __name__ == "__main__":
    assert remove_substring("ABCDEFG", "CDE") == "ABFG"
    assert remove_substring("ABCDEFG", "ABC") == "DEFG"
    assert remove_substring("ABCDEFG", "EEE") == "ABCDEFG"

