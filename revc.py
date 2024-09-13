from utils import load_simple_string_from_text

def complementary_strand(string):

    complementary_nucleotide = {
        "A" : "T",
        "T" : "A",
        "G" : "C",
        "C" : "G"
    }

    reverse_complement = " "
    
    for nucleotide in string:
        if nucleotide in complementary_nucleotide:
            reverse_complement += complementary_nucleotide[nucleotide]

    reverse_complement = reverse_complement[::-1]
    return reverse_complement
    
data = load_simple_string_from_text("in/revc.txt")

with open("out/revc.txt", "w") as file:
    file.write(complementary_strand(data))