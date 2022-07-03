#!/usr/bin/env python
# coding: utf-8

# In[282]:


import os
import fnmatch

# Aggiungo il nome del file del trascrittoma
nomedeltrascrittoma = ""

for ognifile in os.listdir("./"):
    if fnmatch.fnmatch(ognifile, "*.fasta"):
        nomedeltrascrittoma = ognifile

# In[283]:


import pandas as pd

header = "target_name,accession,tlen,query_name,accession1,qlen,E-value,score,bias,#,of,c-Evalue,i-Evalue,score,bias,from,to,START,END,START_envelope,END_envelope,acc,description_of_target\n"

with open("004_sequences_list_SP+DOMAIN_extracted.fasta", "w") as new_file:
    new_file.write(header)

with open("003_sequences_list_SP+DOMAIN", "r") as file:
    for ogniriga in file:
        if ogniriga[0] == "#":
            pass
        else:
            a = ogniriga
            a = a.replace("- ", "empty")
            a = a.replace("  ", " ")
            a = a.replace(" ", ",")
            a = a.replace(",,,", ",")
            a = a.replace(",,", ",")
            a = a.replace(",,", ",")
            # print(a)
            with open("004_sequences_list_SP+DOMAIN_extracted.fasta", "a") as new_file:
                new_file.write(a)

# In[284]:


df = pd.read_csv("004_sequences_list_SP+DOMAIN_extracted.fasta")

# In[285]:


df_selected = df[["target_name", "query_name", "accession1", "START_envelope", "END_envelope"]]
# df_selected


# In[286]:


df_selected.to_csv("005_table_data.tsv", sep="\t")

# In[287]:


import csv
from Bio import SearchIO, SeqIO

temp_list_of_sequence = []
temp_row_to_add = []
dict_seq = {}

counter = 0

with open("005_table_data.tsv", "r") as file_tsv:
    reader = csv.reader(file_tsv, delimiter='\t')
    for row in reader:
        if row[0] != "":
            temp_row_to_add.append(row[1])
            temp_row_to_add.append(row[2])
            temp_row_to_add.append(row[3])
            temp_row_to_add.append(row[4])
            temp_row_to_add.append(row[5])
            dict_seq[counter] = temp_row_to_add
            temp_row_to_add = []
            counter += 1

with open(nomedeltrascrittoma, "r") as file_fasta:
    for record in SeqIO.parse(file_fasta, "fasta"):
        for everyelement in dict_seq:
            if dict_seq[everyelement][0] == record.id:
                dict_seq[everyelement].append(record.seq)

# In[288]:


seq_already_written = []
with open("006_sequences_SP+Domain_Extracted.fasta", "w") as extraction_part1:
    pass
with open("006_sequences_SP+Domain_Extracted.fasta", "a") as extraction_part2:
    for everyelement in dict_seq:
        if dict_seq[everyelement][0] in seq_already_written:
            pass
        else:
            extraction_part2.write(f">{dict_seq[everyelement][0]}\n{dict_seq[everyelement][5]}\n\n")
            seq_already_written.append(dict_seq[everyelement][0])

# Reading the log
counter_log = ""
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
            extraction_part2.write(f">{dict_seq[everyelement][0]}\n{dict_seq[everyelement][5]}\n\n")
            seq_already_written.append(dict_seq[everyelement][0])

with open("007_domain_sequences_extracted.fasta", "a") as extraction_part3:
    for everyelement in dict_seq:
        domain = str(dict_seq[everyelement][5])
        extraction_part3.write(
            f">{dict_seq[everyelement][0]} - from {dict_seq[everyelement][3]} to {dict_seq[everyelement][4]}\n{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n")

nome_file = f"../Research_number_{counter_log2[:-1]}_OUTPUT-FOLDER/002_all_domains_extracted.fasta"

with open(nome_file, "a") as extraction_part4:
    for everyelement in dict_seq:
        domain = str(dict_seq[everyelement][5])
        extraction_part4.write(
            f">{dict_seq[everyelement][0]} - from {dict_seq[everyelement][3]} to {dict_seq[everyelement][4]}\n{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n")

# In[ ]:



