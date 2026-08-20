import sys

# Load data from argument
with open(sys.argv[1], "r") as f:
    dna = f.read()

# Function to count nucleotides in order: A C G T
def count_nucleotide(dna):
    nucleotide_count = { "A": 0, "C": 0, "G": 0, "T": 0 }
    for nucleotide in dna:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide] += 1
    return f'{nucleotide_count["A"]} {nucleotide_count["C"]} {nucleotide_count["G"]} {nucleotide_count["T"]}'

# Print result to stdout
print(count_nucleotide(dna))

    



