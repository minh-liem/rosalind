from Bio import SeqIO

def read_fasta(file_path):
    return [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]

def longest_common_substring(strings):
    # Use the shortest string to minimize search space
    shortest = min(strings, key=len)
    n = len(shortest)
    
    # Try substrings of decreasing length
    for length in range(n, 0, -1):
        for i in range(n - length + 1):
            candidate = shortest[i:i+length]
            if all(candidate in s for s in strings):
                return candidate
    return ""

# Example usage:
fasta_path = "in/lcsm.txt"  # replace with your FASTA file path
sequences = read_fasta(fasta_path)
result = longest_common_substring(sequences)
print(result)

