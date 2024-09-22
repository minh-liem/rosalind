from utils import load_simple_string_from_text
from math import log10

def random_string(string, probs):
    out = []

    for i in range(len(probs)):
        string_prob = 1

        nuc_prob = {
        "A" : (1-probs[i])/2,
        "C" : probs[i]/2,
        "G" : probs[i]/2,
        "T" : (1-probs[i])/2
        }

        for ii in string:
            string_prob = string_prob*nuc_prob[ii]
        
        out.append(round(log10(string_prob),3))
    
    out_str = ' '.join(str(iii) for iii in out)

    return out_str

data = load_simple_string_from_text("in/prob.txt")
data = data.split('\n')

run_string = data[0]
run_probs = [float(x) for x in data[1].split()]

with open("out/prob.txt", "w") as file:
    file.write(random_string(run_string, run_probs))

        
        
        




    

