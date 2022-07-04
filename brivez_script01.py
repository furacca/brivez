#!/usr/bin/env python
# coding: utf-8

# Script - From deepsig to fasta
import fnmatch
import os
import csv
from Bio import SeqIO


# Estrazione sequenze presentanti il SP
sequence_with_sp = []
with open("001_deepsig_output.tsv", "r") as file_tsv:
    reader = csv.reader(file_tsv, delimiter='\t')
    for row in reader:
        if row[2] == "Signal peptide":
            sequence_with_sp.append(row[0])

# Aggiungo il nome del file del trascrittoma
nomedeltrascrittoma = ""
for ognifile in os.listdir("./"):
    if fnmatch.fnmatch(ognifile, "*.fasta"):
        nomedeltrascrittoma = ognifile

# Prendiamo i nomi delle sequenze identificate sopra e creaiamo un file fasta
name_plus_seq = {}
with open(nomedeltrascrittoma, "r") as file_fasta:
    for record in SeqIO.parse(file_fasta, "fasta"):
        for every_name_of_seq in sequence_with_sp:
            if record.id == every_name_of_seq:
                name_plus_seq[record.id] = record.seq

# print(name_plus_seq)
with open("002_deepsig_sequence_with_SP.fa", "w") as file:
    for everyelement in name_plus_seq:
        file.write(f">{everyelement}\n{name_plus_seq[everyelement]}\n\n")
