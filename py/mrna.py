from dictionaries import codon_to_amino_acid
from utils import load_simple_string_from_text


def inferring_mrna(protein_string):
    possible_string = 1
    for aa in protein_string:
        if aa in codon_to_amino_acid.values():
            possible_string = possible_string * len([codon for codon, amino_acid in codon_to_amino_acid.items() if amino_acid == aa])
    
    possible_string = possible_string * len([codon for codon, amino_acid in codon_to_amino_acid.items() if amino_acid == "*"])

    return str(possible_string % 1000000)


data = load_simple_string_from_text("in/mrna.txt")
with open("out/mrna.txt","w") as file:
    file.write(inferring_mrna(data))
