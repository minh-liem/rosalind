from dictionaries import codon_to_amino_acid
from utils import load_simple_string_from_text

def rna_to_protein(str):
    protein_sequence = ""
    i = 0
    while i in range (len(str) - 3 + 1):
        codon = str[i:i+3]
        aa = codon_to_amino_acid[codon]
        if aa == "*":
            return protein_sequence
        protein_sequence += aa
        i += 3
    return protein_sequence

data = load_simple_string_from_text("in/prot.txt")

with open ("out/prot.txt", "w") as file:
    file.write(rna_to_protein(data))
