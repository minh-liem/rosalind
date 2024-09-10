# Load data
dna = open("data/dna.txt", "r").read()

# Function to count nucleotide in a given dna string of order: A, C, G, T

def count_nucleotide(dna):
    # Initialize dictionary
    nucleotide_count = {
        "A" : 0,
        "C" : 0, 
        "G" : 0,
        "T" : 0
    }

    for nucleotide in dna:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide] += 1
    
    return f'{nucleotide_count["A"]} {nucleotide_count["C"]} {nucleotide_count["G"]} {nucleotide_count["T"]}'

print(count_nucleotide(dna))
    



