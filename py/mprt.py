from pathlib import Path
from utils import load_sequences

prot_seq_dir = Path("in/mprt")
motif = {}


for fasta in prot_seq_dir.iterdir():
    id = fasta.stem
    prot_seq = load_sequences(fasta)[0][1]

    for motif_index in range (0, len(prot_seq)-3):
            if prot_seq[motif_index] == 'N' and prot_seq[motif_index+1] != "P" and (prot_seq[motif_index+2] == "S" or prot_seq[motif_index+2] =="T") and prot_seq[motif_index+3]!="P":
                if id not in motif:
                        motif[id] = [motif_index+1]
                else:
                        motif[id].append(motif_index+1)


with open("out/mprt.txt", "w") as out:
      for ids in motif:
            out.write(f"{ids} \n")
            out.write(' '.join(str(loc) for loc in motif[ids]))
            out.write("\n")


