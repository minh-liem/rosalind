from itertools import permutations
from utils import read_file_as_integers

def possible_perm(int):
    elements = []
    for index in range(int):
        elements.append(index+1)
    
    perm_list = []
    for perm in permutations(elements):
        perm_list.append(perm)
    
    perm_string_list = []
    for perm in perm_list:
        perm_string_list.append(' '.join(map(str, perm)))
    
    return f"{len(perm_list)}\n" + '\n'.join(perm_string_list)

data = read_file_as_integers("in/perm.txt")
data = data[0]

with open("out/perm.txt", "w") as file:
    file.write(possible_perm(data))
    


    
    