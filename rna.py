from utils import load_simple_string_from_text

def dna_to_rna(string):
    for nucleotide in string:
        if nucleotide == "T":
            string = string.replace(nucleotide, "U")
    
    return string

data = load_simple_string_from_text("in/rna.txt")

with open("out/rna.txt", "w") as file:
    file.write(dna_to_rna(data))

