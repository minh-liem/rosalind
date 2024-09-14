from utils import load_simple_string_from_text

def hamming_distance(str1, str2):
    hamming_distance = 0

    for nucletide in range(len(str1)):
        if str1[nucletide] != str2[nucletide]:
            hamming_distance += 1
    
    return hamming_distance

data = load_simple_string_from_text("in/hamm.txt")
seqs = data.splitlines()

with open("out/hamm.txt", "w") as file:
    file.write(str(hamming_distance(seqs[0], seqs[1])))