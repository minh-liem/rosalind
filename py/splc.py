from utils import load_sequences 
from dictionaries import codon_to_amino_acid
from rna import dna_to_rna
from prot import rna_to_protein


def splicing(fasta_tuple):
    original_sequence = fasta_tuple[0][1]

    for intron_tuple in fasta_tuple[1:]:
        original_sequence = original_sequence.replace(intron_tuple[1], '')
    
    return(rna_to_protein(dna_to_rna(original_sequence)))

data = load_sequences("in/splc.txt")

with open("out/splc.txt", "w") as file:
    file.write(splicing(data))
    


