from utils import load_simple_string_from_text

input = load_simple_string_from_text("in/ini6.txt").strip("\n").split(' ')

dict = {}

for word in input:
    if word not in dict.keys():
        dict[word] = 1
    else:
        dict[word] += 1

with open("out/ini6.txt", "w") as out:
    for word in dict.keys():
        out.write(f"{word} {dict[word]}\n")