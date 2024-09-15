# Funcs to load data
def load_sequences(filepath: str):
    from Bio import SeqIO
    seqs = []
    for seq in SeqIO.parse(filepath, "fasta"):
        seqs.append((seq.name, str(seq.seq)))
    return seqs

def load_simple_string_from_text(filepath: str):
    with open(filepath, "r") as file:
        string = file.read()
    return string
