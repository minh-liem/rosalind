
with open("in/ini3.txt") as f:
    lines = [line.rstrip("\n") for line in f]
    string = lines[0]
    indexes = list(map(int, lines[1].split()))

with open("out/ini3.txt", "w") as out:
    out.write(f"{string[indexes[0]:indexes[1]+1]} {string[indexes[2]:indexes[3]+1]}")


