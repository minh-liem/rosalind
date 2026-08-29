letters = ['A', 'T', 'G', 'C']
n = 4
init_string = letters[0]*n
list = [init_string]


for i in range (0, n):
    for letter_index in range(1, len(letters)):
        init_string = init_string.replace(init_string[i], letters[letter_index]) 
        list.append(init_string)
        if i > 0:
            for ii in range(0, i):
                init_string = init_string.replace(init_string[ii], letters[letter_index]) 
                list.append(init_string)

string = "AAAA"

print(string[1])
string = string.replace(string[1], "T", 2)

print(string)