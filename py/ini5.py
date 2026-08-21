
with open("in/ini5.txt") as f: 
    lines = f.readlines()
    with open("out/ini5.txt", "w") as out:
        out.writelines(lines[i+1] for i in range(len(lines)) if i % 2 ==0)
