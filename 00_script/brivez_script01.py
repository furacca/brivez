#!/usr/bin/env python
# coding: utf-8

# --------------------------------------------------------------
# What this script does?

# --------------------------------------------------------------
# Importing some libraries
import fnmatch
import os
import csv
from Bio import SeqIO

# --------------------------------------------------------------
# Counter for selected sequences (used by brivez_main.sh in final report)
sequencecounter = 0

# --------------------------------------------------------------
# Deepsig output's path
deepsig_output_path = "./tmp_output/01_deepsig-analysis.tsv"

# --------------------------------------------------------------
# Obtaining fasta source name
datafilename = ""
for everyfile in os.listdir("./"):
    if fnmatch.fnmatch(everyfile, "ROTFLMAO*"):
        datafilename = everyfile
datafilerootname = datafilename.replace("ROTFLMAO","")

# --------------------------------------------------------------
# Checking if deepsig analysis has been deactivated
deepsig_has_been_deactivated = "false"
with open(deepsig_output_path, "r") as file_tsv:
    reader = csv.reader(file_tsv, delimiter='\t')
    for row in reader:
        if row[2] == "not":
            deepsig_has_been_deactivated = "true"
            os.rename("tmp_output/01_deepsig-analysis.tsv", "tmp_output/01_deepsig_DISABLED") 
            break
        else:
            break

# --------------------------------------------------------------
# Creating the list of sequence that need to be selected
sequence_target_s_name = []

if deepsig_has_been_deactivated == "false":
    # Selecting all the sequences with Signal Peptide 
    with open(deepsig_output_path, "r") as file_tsv:
        tsv_read = csv.reader(file_tsv, delimiter='\t')
        for row in tsv_read:
            if row[2] == "Signal peptide":
                sequence_target_s_name.append(row[0])
                
elif deepsig_has_been_deactivated == "true":
    # Selecting all the sequences
    with open(datafilerootname, "r") as file_fasta:
        for record in SeqIO.parse(file_fasta, "fasta"):
        	sequence_target_s_name.append(record.id)


# --------------------------------------------------------------
# Selecting the sequence for every name in sequence_target_s_name list
sequencename_plus_sequence = {}

with open(datafilerootname, "r") as file_fasta:
    for record in SeqIO.parse(file_fasta, "fasta"):
        for eachname in sequence_target_s_name:
            if record.id == eachname:
                sequencename_plus_sequence[record.id] = record.seq
                sequencecounter += 1

# --------------------------------------------------------------
# Printing the something in the CLI
cmd = f"""echo "{sequencecounter} sequence(s) selected" """
os.system(cmd)

# --------------------------------------------------------------
# Saving [sequencename + sequence] in fasta file
with open("./tmp_output/02_sequences_selected.fasta", "w") as file:
    for everyelement in sequencename_plus_sequence:
        file.write(f">{everyelement}\n{sequencename_plus_sequence[everyelement]}\n\n")

print("Created -------->    02_sequences_selected.fasta")
