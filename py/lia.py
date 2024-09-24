from math import comb
from utils import read_file_as_integers


def AaBb_progeny(k, n):
    num_children = 2**k
    Pr_at_most_n_minus_1_AaBb_children = 0

    for i in range(n):
        Pr_i_AaBb_children = comb(num_children, i) * (1/4)**i * (3/4)**(num_children-i)
        Pr_at_most_n_minus_1_AaBb_children += Pr_i_AaBb_children


    Pr_at_least_n_AaBb_children = 1 - Pr_at_most_n_minus_1_AaBb_children
    return str(round(Pr_at_least_n_AaBb_children,3))


data = read_file_as_integers("in/lia.txt")
k = data[0]
n = data[1]

with open("out/lia.txt", "w") as file:
    file.write(AaBb_progeny(k, n))
