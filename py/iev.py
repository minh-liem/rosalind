from utils import read_file_as_integers
from dictionaries import dominant_allele_offspring_probability

def expected_dominant_offspring(a, b, c, d, e, f):
    # Define a list of the counts and corresponding probabilities
    pairs = [
        (a, ('AA', 'AA')),
        (b, ('AA', 'Aa')),
        (c, ('AA', 'aa')),
        (d, ('Aa', 'Aa')),
        (e, ('Aa', 'aa')),
        (f, ('aa', 'aa'))
    ]

    # Calculate the total expected dominant offspring
    total = 0
    for count, pair in pairs:
        total += count * dominant_allele_offspring_probability[pair][0]
    
    # Multiply by 2 as each pair produces two offspring
    return str(2 * total)

file_path = "in/iev.txt"

data = read_file_as_integers(file_path)

with open("out/iev.txt", "w") as file:
    file.write(expected_dominant_offspring(data[0], data[1], data[2], data[3], data[4], data[5]))