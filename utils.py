def load_sequences(filepath: str):
    from Bio import SeqIO
    seqs = []
    for seq in SeqIO.parse(filepath, "fasta"):
        seqs.append((seq.name, str(seq.seq)))
    return seqs