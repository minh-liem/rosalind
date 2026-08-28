with open("in/pper.txt", "r") as file:
    input = file.readline().split(" ")


n = int(input[0])
k = int(input[1])

def calculate_partial_perm(n, k):
    res = 1
    for i in range(n-k+1, n+1):
        res = res * i
    return res

with open("out/pper.txt", "w") as out:
    out.write(f"{calculate_partial_perm(n,k) % 1000000}")