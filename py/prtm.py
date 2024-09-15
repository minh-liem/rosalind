from utils import load_simple_string_from_text
from dictionaries import amino_acid_mass_table

def protein_mass_calculator(sequence):
    mass = 0 
    for amino_acid in sequence:
        if amino_acid in amino_acid_mass_table:
            mass += amino_acid_mass_table[amino_acid]
    
    return round(mass, 3)

data = load_simple_string_from_text("in/prtm.txt")

with open("out/prtm.txt", "w") as file:
    file.write(str(protein_mass_calculator(data)))