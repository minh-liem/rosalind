from utils import load_sequences

def overlap_graphs(sequences):
    name_list = list(sequences[i][0] for i in range(len(sequences)))
    seq_list = list(sequences[i][1] for i in range(len(sequences)))
    edges = []
    
    for s in seq_list:
        for t in seq_list: 
            if t != s:
                if s[-3:] == t[0:3]:
                    edges.append((name_list[seq_list.index(s)], name_list[seq_list.index(t)]))
                
    edges_str = '\n'.join(f"{x} {y}" for x, y in edges)

    return edges_str

data = load_sequences("in/grph.txt")

with open("out/grph.txt", "w") as file:
    file.write(overlap_graphs(data))

