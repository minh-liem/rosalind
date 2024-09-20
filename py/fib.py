from utils import read_file_as_integers


def fibo_rabbit(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (fibo_rabbit(n-1, k) + fibo_rabbit(n-2, k)*k)
    
data = read_file_as_integers("in/fib.txt")

n = data[0]
k = data[1]

with open("out/fib.txt", "w") as file:
    file.write(str(fibo_rabbit(n, k)))

