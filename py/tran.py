from utils import load_sequences

def transition_transversion_ratio(data):
    sequence_1 = data[0][1]
    sequence_2 = data[1][1]
    transition = 0
    tranversion = 0

    for nucleotide in range(0, len(sequence_1)):
        if sequence_1[nucleotide] != sequence_2[nucleotide]:
            if (sequence_1[nucleotide], sequence_2[nucleotide]) in [("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")]:
                transition += 1
            else:
                tranversion += 1
    
    return str(round(transition/tranversion, 11))

data = load_sequences("in/tran.txt")
with open("out/tran.txt", "w") as file:
    file.write(transition_transversion_ratio(data))
