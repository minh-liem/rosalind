from utils import load_sequences

def highest_gc(seqs):
    gc_content = []

    for seq_tuple in seqs:
        gc_content.append((seq_tuple[1].count('G') + seq_tuple[1].count('C'))/len(seq_tuple[1]))
    
    max_index = gc_content.index(max(gc_content))
    return f"{seqs[max_index][0]}\n{round((max(gc_content)*100), 6)}"\


data = load_sequences("data/gc_content.txt")
print(highest_gc(data))

