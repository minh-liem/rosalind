from utils import read_file_as_integers
from math import sqrt


def sq_hypo_right_triangle(a,b):
    return str(round(sqrt(a**2+b**2)**2))

file_path="in/ini2.txt"
legs = read_file_as_integers(file_path)

with open("out/ini2.txt", "w") as file:
    file.write(sq_hypo_right_triangle(legs[0], legs[1]))