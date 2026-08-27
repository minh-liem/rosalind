from utils import load_sequences



string = load_sequences("in/revp.txt")[0][1]
rev = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
reverse_comp = ''.join(rev[b] for b in string)
list = []

for length in range(4, 13):
        for index in range(0, len(string)-length+1):
            string_to_check = string[index:index+length]
            rev_check = reverse_comp[index:index+length]
            if string_to_check == rev_check[::-1]:
                list.append([index+1, length])
                

with open("out/revp.txt", "w") as out:
    for pos_and_length in list:
         out.write(f"{pos_and_length[0]} {pos_and_length[1]} \n")