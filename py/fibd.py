from utils import read_file_as_integers

def mortal_fib_rabbit(n, k):
    ages = [1] + [0]*(k-1)
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return str(sum(ages))

data = read_file_as_integers("in/fibd.txt")
n = data[0]
k = data[1]

with open("out/fibd.txt", "w") as file:
    file.write(mortal_fib_rabbit(data[0], data[1]))