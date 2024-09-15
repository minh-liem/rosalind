from utils import load_simple_string_from_text

def substring_location(s, t):
    location = []

    for index in range(0, len(s) - len(t) + 1):
        if s[index:index+len(t)] == t:
            location.append(index + 1) # Location = Index + 1 
    
    return ' '.join(map(str, location))

data = load_simple_string_from_text("in/subs.txt")
s = data.splitlines()[0]
t = data.splitlines()[1]

with open("out/subs.txt", "w") as file:
    file.write(substring_location(s, t))


