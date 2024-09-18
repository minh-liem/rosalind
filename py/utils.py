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

def read_file_as_integers(file_path):
    with open(file_path, 'r') as file:
        # Read the line and split it into a list of strings
        line = file.readline().strip()
        # Convert the list of strings to a list of integers
        k, m, n = map(int, line.split())
    return k, m, n