from utils import load_sequences

def consensus_profile(sequences):
    seq_length = len(sequences[0][1])
    seqs = [seq[1] for seq in sequences]

    count_dict = {
        "A" : [0] * seq_length,
        "C" : [0] * seq_length,
        "G" : [0] * seq_length,
        "T" : [0] * seq_length,
    }

    for nuc_index in range(seq_length):
        for seq in seqs: 
            count_dict[seq[nuc_index]][nuc_index] += 1
    
    consensus_seq = ''
    for nuc_index in range(seq_length):
        max_nuc = max(count_dict.keys(), key=lambda nuc: count_dict[nuc][nuc_index])
        consensus_seq += max_nuc

    def format_out(consensus_seq, count_dict):
        formatted_count = []

        for nuc, counts in count_dict.items():
            formatted_count.append(f"{nuc}: {' '.join(map(str, counts))}")
        
        formatted_count_to_str = '\n'.join(formatted_count)

        return f"{consensus_seq}\n{formatted_count_to_str}"
    
    return format_out(consensus_seq, count_dict)

data = load_sequences("in/cons.txt")

with open("out/cons.txt", "w") as file:
    file.write(consensus_profile(data))