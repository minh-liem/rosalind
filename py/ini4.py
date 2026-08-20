from utils import read_file_as_integers

data = read_file_as_integers("in/ini4.txt")

def count_sum(ints):
    sum = 0
    for num in range(ints[0], ints[1]+1):
        if num % 2 == 1:
            sum += num
    return str(sum)

with open("out/ini4.txt", "w") as f:
    f.write(count_sum(data))
