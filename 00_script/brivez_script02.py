#!/usr/bin/env python
# coding: utf-8

# From domtblout to seqfastalist and domains fasta list

import os
import fnmatch
import csv
import pandas as pd
from Bio import SeqIO

# Aggiungo il nome del file del trascrittoma
nomedeltrascrittoma = ""

for ognifile in os.listdir("./"):
    if fnmatch.fnmatch(ognifile, "*.fasta"):
        nomedeltrascrittoma = ognifile

header = "target_name,accession,tlen,query_name,accession1,qlen,E-value,score,bias,#,of,c-Evalue,i-Evalue,score,bias," \
         "from,to,START_ali,END_ali,START_envelope,END_envelope,acc,description_of_target\n"

with open("004_hmmer_output_table_data_parsed", "w") as new_file:
    new_file.write(header)

with open("003_hmmer_output_table", "r") as file:
    for ogniriga in file:
        if ogniriga[0] == "#":
            pass
        else:
            a = ogniriga
            a = a.replace("- ", "empty")
            a = a.replace("  ", " ")
            a = a.replace("  ", " ")
            a = a.replace("  ", " ")
            a = a.replace("  ", " ")
            a = a.replace("  ", " ")
            a = a.replace("  ", " ")
            a = a.replace(" ", ",")
            with open("004_hmmer_output_table_data_parsed", "a") as new_file:
                new_file.write(a)

df = pd.read_csv("004_hmmer_output_table_data_parsed")
df_selected = df[["target_name", "query_name", "accession1", "START_ali", "END_ali"]]
df_selected.to_csv("005_pandas_sequences_table.tsv", sep="\t")

temp_list_of_sequence = []
temp_row_to_add = []
dict_seq = {}

counter = 0

with open("005_pandas_sequences_table.tsv", "r") as file_tsv:
    reader = csv.reader(file_tsv, delimiter='\t')
    for row in reader:
        if row[0] != "":
            temp_row_to_add.append(row[1])
            temp_row_to_add.append(row[2])
            temp_row_to_add.append(row[3])
            temp_row_to_add.append(row[4])
            temp_row_to_add.append(row[5])
            # Ex.1 - temp_row_to_add = ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1667', '1870']
            dict_seq[counter] = temp_row_to_add
            temp_row_to_add = []
            counter += 1

# Dizionario a fine ciclo : {0: [' sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1259', '1463'],
# 1: ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1485', '1657'], 2: ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty',
# '1667', '1870']}



# EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

name_list_of_all_seq = []
char_to_remove = 0

with open(nomedeltrascrittoma, "r") as file_fasta:
    for everysequence in SeqIO.parse(file_fasta, "fasta"):
        name_list_of_all_seq.append(everysequence.id)

if len(name_list_of_all_seq) == 1:
    pass
else:
    # Guardo la lunghezza minima delle sequenze
    word_len = 100
    for everyword in name_list_of_all_seq:
        if len(everyword) < word_len:
            word_len = len(everyword)
        else:
            pass
    # Calcolo quante lettere ci sono da eliminare

    a = 0
    for everytime in range(0, word_len):
        char_check = []

        for everyelement in name_list_of_all_seq:
            if everyelement[a] in char_check:
                pass
            else:
                char_check.append(everyelement[a])

        if len(char_check) == 1:
            char_to_remove += 1
        a += 1

# EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

root = nomedeltrascrittoma.replace(".fasta", "")

with open(nomedeltrascrittoma, "r") as file_fasta:
    for record in SeqIO.parse(file_fasta, "fasta"):
        for everyelement in dict_seq:
            if dict_seq[everyelement][0] == record.id:
                dict_seq[everyelement].append(record.seq)

seq_already_written = []
with open("006_sequence_with_SP+Domain_extracted.fa", "w") as extraction_part1:
    pass
with open("006_sequence_with_SP+Domain_extracted.fa", "a") as extraction_part2:
    for everyelement in dict_seq:
        if dict_seq[everyelement][0] in seq_already_written:
            pass
        else:
            extraction_part2.write(f">{root}_{dict_seq[everyelement][0][char_to_remove:]}\n{dict_seq[everyelement][5]}\n\n")
            seq_already_written.append(dict_seq[everyelement][0])

# Reading the log
with open("../log", "r") as file:
    counter_log = file.read()
counter_log2 = str(counter_log)

seq_already_written = []
with open(f"../Research_number_{counter_log2[:-1]}_OUTPUT-FOLDER/001_all_sequences_extracted.fasta",
          "a") as extraction_part2:
    for everyelement in dict_seq:
        if dict_seq[everyelement][0] in seq_already_written:
            pass
        else:
            extraction_part2.write(f">{root}_{dict_seq[everyelement][0][char_to_remove:]}\n{dict_seq[everyelement][5]}\n\n")
            seq_already_written.append(dict_seq[everyelement][0])

with open("007_domains_of_sequences_with_SP+Domain_extracted.fa", "a") as extraction_part3:
    for everyelement in dict_seq:
        domain = str(dict_seq[everyelement][5])
        extraction_part3.write(
            f">{root}_{dict_seq[everyelement][0][char_to_remove:]}-{dict_seq[everyelement][1]}-from{dict_seq[everyelement][3]}to{dict_seq[everyelement][4]}\n{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n")

nome_file = f"../Research_number_{counter_log2[:-1]}_OUTPUT-FOLDER/002_all_domains_extracted.fasta"

with open(nome_file, "a") as extraction_part4:
    for everyelement in dict_seq:
        domain = str(dict_seq[everyelement][5])
        extraction_part4.write(
            f">{root}_{dict_seq[everyelement][0][char_to_remove:]}-{dict_seq[everyelement][1]}-from{dict_seq[everyelement][3]}to{dict_seq[everyelement][4]}\n{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n")


