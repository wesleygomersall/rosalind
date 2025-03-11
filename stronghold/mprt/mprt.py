#!/usr/bin/env python

# https://rosalind.info/problems/mprt/

from parsefasta import get_args
import json

# curl --form 'from="UniProtKB_AC-ID"' \
     # --form 'to="UniProtKB"' \
     # --form 'ids="A2Z669,B5ZC00,P07204_TRBM_HUMAN,P20840_SAG1_YEAST"' \
     # https://rest.uniprot.org/idmapping/run

def main():
    with open(get_args().input, 'r') as fin:
        jin = json.load(fin)
        seq = jin['results']

# The asparagine-X-serine/threonine (NXS/T) motif, 
# where X is any amino acid except proline, 
# is the consensus motif for N-linked glycosylation. 
#
# Lam PV, Goldman R, Karagiannis K, Narsule T, Simonyan V, Soika V, Mazumder R. Structure-based comparative analysis and prediction of N-linked glycosylation sites in evolutionarily distant eukaryotes. Genomics Proteomics Bioinformatics. 2013 Apr;11(2):96-104. doi: 10.1016/j.gpb.2012.11.003. Epub 2013 Feb 28. PMID: 23459159; PMCID: PMC3914773.

if __name__ == "__main__":
    main()
