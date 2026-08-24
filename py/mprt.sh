#!/usr/bin/env bash

INPUT="../in/mprt.txt"

while IFS= read -r ID || [ -n "$ID" ]; do
    ACCESSION="${ID%%_*}"
    wget http://www.uniprot.org/uniprot/${ACCESSION}.fasta -O ../in/mprt/${ID}.fasta
done < "$INPUT"

