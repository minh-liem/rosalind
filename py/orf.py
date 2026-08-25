from dictionaries import codon_to_amino_acid
from utils import load_sequences



def open_reading_frames(filepath):
    input_dna = load_sequences(filepath)[0][1]
    rna = input_dna.replace("T", "U")
    comp = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    rna_rev = ''.join(comp[b] for b in reversed(rna))
    return rna, rna_rev

    
    

prot_strings = []

def distinct_protein(original_string):
    for frame_start in range(0,3):
        framed_string = original_string[frame_start:]
        
        for nucleotide_index in range(0, len(framed_string)-2):
            prot = ''
            codon = framed_string[nucleotide_index:nucleotide_index+3]

            if codon_to_amino_acid[codon] == 'M':
                while nucleotide_index < len(framed_string)-3:
                    prot += codon_to_amino_acid[codon]
                    nucleotide_index += 3
                    codon = framed_string[nucleotide_index:nucleotide_index+3]
        
            if prot != '' and "*" in prot:
                if prot[:prot.index("*")] not in prot_strings:
                    prot_strings.append(prot[:prot.index("*")])

    return(prot_strings)

rna, rna_rev = open_reading_frames("in/orf.txt")
fwd = distinct_protein(rna)
rev = distinct_protein(rna_rev)

protein_list = list(set(fwd) | set(rev))

with open("out/orf.txt", "w") as out:
    for protein in protein_list:
        out.write(f"{protein} \n")      



    



    
 


