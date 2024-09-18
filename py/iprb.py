from utils import read_file_as_integers
from dictionaries import dominant_allele_offspring_probability
import math

def dominant_allele_probability(k, m, n):
    # Sample contains: k AA, m Aa, n aa

    total = k + m + n
    total_pair = (total*(total - 1))/2

    expected_dominant_offspring = 0

    for pair in dominant_allele_offspring_probability.keys():
        if pair[0] == pair[1]:
            if pair[0] == 'AA':
                expected_dominant_offspring += math.comb(k, 2) * dominant_allele_offspring_probability[('AA', 'AA')][0]
            elif pair[0] == 'Aa':
                expected_dominant_offspring += math.comb(m, 2) * dominant_allele_offspring_probability[('Aa', 'Aa')][0]
            else:
                expected_dominant_offspring += math.comb(n, 2) * dominant_allele_offspring_probability[('aa', 'aa')][0]
        else:
            if pair[0] == 'AA' and pair[1] == 'Aa':
                expected_dominant_offspring += (k * m)*dominant_allele_offspring_probability[('AA', 'Aa')][0]
            elif pair[0] == 'AA' and pair[1] == 'aa':
                expected_dominant_offspring += (k * n)*dominant_allele_offspring_probability[('AA', 'aa')][0]
            else: 
                expected_dominant_offspring += (m * n)*dominant_allele_offspring_probability[('Aa', 'aa')][0]
        
    return str(round(expected_dominant_offspring/total_pair, 5))

file_path = "in/iprb.txt"

k, m, n = read_file_as_integers(file_path)

with open("out/iprb.txt", "w") as file:
    file.write(dominant_allele_probability(k, m, n))



