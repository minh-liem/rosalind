path = 'AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB'
prob = 0.5

with open("in/ba10a.txt", "r") as input:
    content = input.readlines()
    path = content[0].strip("\n")
    prob = 1/len(content[4].strip().split())



matrix = {
    'A' : {
        'A': float(content[5].strip().strip('A').split()[0]),
        'B': float(content[5].strip().strip('A').split()[1])
    },
    'B' : {
        'A': float(content[6].strip().strip('B').split()[0]),
        'B': float(content[6].strip().strip('B').split()[1])
    }

}



for i in range (0,len(path)-1):
    prob = prob * matrix[path[i]][path[i+1]]



with open("out/ba10a.txt", "w") as out:
    out.write(str(prob))


