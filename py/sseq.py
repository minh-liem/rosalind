from utils import load_sequences

def greedy_subseq_indeces(str1, str2):
    indices = []

    for nuc2 in str2:

        current_nuc1_pos = 1
        for nuc1 in str1:
            if nuc1 == nuc2:
                if len(indices) == 0:
                    indices.append(current_nuc1_pos)
                    break
                elif current_nuc1_pos > indices[-1]:
                    indices.append(current_nuc1_pos)
                    break
            current_nuc1_pos += 1
            
    
    return indices
            
data = load_sequences("in/sseq.txt")
str1 = data[0][1]
str2 = data[1][1]

output = ' '.join(map(str, greedy_subseq_indeces(str1, str2)))

with open("out/sseq.txt", "w") as file:
    file.write(output)
    
