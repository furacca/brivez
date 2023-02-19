#!/usr/bin/env python
# coding: utf-8

# --------------------------------------------------------------
# What this script does?
# Good question.

# --------------------------------------------------------------
# Importing some libraries
import os
import fnmatch
import csv
import pandas as pd
from Bio import SeqIO


# --------------------------------------------------------------
# Defining some functions


def print_message(outputfilenumber):
	print(f"Created -------->    {outputfilenumber}")


# --------------------------------------------------------------
# Defining the output files' name

file_04 = "04_hmmsearch_output_table_data_parsed"
file_05 = "05_pandas_sequences_table.tsv"
file_06 = "06_sequences_which_have_domains.fasta"
file_07 = "07_extracted_domains.fasta"
file_08 = "08_extracted_domains.csv"
file_09 = "09_REPORT"

# --------------------------------------------------------------
# Output's path
output_path = "./tmp_output"

# --------------------------------------------------------------
# Obtaining fasta source name
datafilename = ""
for everyfile in os.listdir("./"):
    if fnmatch.fnmatch(everyfile, "ROTFLMAO*"):
        datafilename = everyfile
fastasource = datafilename.replace("ROTFLMAO", "")

# --------------------------------------------------------------
# Reading and parsing the hmmsearch output file

# Setting up the header (for pandas) and write it inside 04_hmmsearch_output_table_data_parsed
header = "target_name,accession,tlen,query_name,accession1,qlen,E-value,score,bias,#,of,c-Evalue,i-Evalue,score,bias," \
         "from,to,START_ali,END_ali,START_envelope,END_envelope,acc,description_of_target\n"

with open(f"{output_path}/04_hmmsearch_output_table_data_parsed", "w") as new_file:
    new_file.write(header)

with open(f"{output_path}/03_hmmsearch_output_table", "r") as file:
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
            with open(f"{output_path}/04_hmmsearch_output_table_data_parsed", "a") as filetomod:
                filetomod.write(a)

# Creating a pandas dataframe
df = pd.read_csv(f"{output_path}/04_hmmsearch_output_table_data_parsed")
print_message(file_04)

# Filtering for the columns of interest
df_selected = df[["target_name", "query_name",
    "accession1", "START_ali", "END_ali"]]

# Saving the filtered columns in tsv file
df_selected.to_csv(f"{output_path}/05_pandas_sequences_table.tsv", sep="\t")
print_message(file_05)

# --------------------------------------------------------------
# Reading and parsing the hmmsearch output file
temp_row_to_add = []
dict_seq = {}

# dict_seq counter
counter = 0


with open(f"{output_path}/05_pandas_sequences_table.tsv", "r") as file_tsv:
    tsvread = csv.reader(file_tsv, delimiter='\t')
    for row in tsvread:
        if row[0] != "":
            # temp_row_to_add = ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1667', '1870']
            temp_row_to_add.append(row[1])
            temp_row_to_add.append(row[2])
            temp_row_to_add.append(row[3])
            temp_row_to_add.append(row[4])
            temp_row_to_add.append(row[5])
            dict_seq[counter] = temp_row_to_add
            temp_row_to_add = []
            counter += 1


#  dict_seq structure
# {
# 0: ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1259', '1463'],
# 1: ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1485', '1657'],
# 2: ['sp|P04275|VWF_HUMAN', 'vwA_MSA', 'empty', '1667', '1870']
# }


# --------------------------------------------------------------
# Checking the common root name for all the sequences, deleting it from the final output
# BEFORE
# >Californicus_californicus_transcriptome_SRR2609536_trimmed_(paired)_contig_23503.p1
# AFTER
# >Californicus_californicus_23503.p1

list_of_names_of_all_sequences = []

with open(fastasource, "r") as file_fastasource:
    for everysequence in SeqIO.parse(file_fastasource, "fasta"):
        list_of_names_of_all_sequences.append(everysequence.id)

# Looking for the length of the shortest sequence
# If you have just one sequence, you can't determine which is the root (you need two sequences or more)


# Set the chars need to be removed to zero
char_to_be_removed_counter = 0

if len(list_of_names_of_all_sequences) > 1:

    shortest_sequence_lenght = 1000

    for eachname in list_of_names_of_all_sequences:
        if len(eachname) < shortest_sequence_lenght:
            shortest_sequence_lenght = len(eachname)

    # x = position (in the common root) of each char
    for x in range(0, shortest_sequence_lenght):

        # List of char found in the range; if len(char_check) > 1 then there are two different char for that position -> this is where the common root ends
        char_check = []

        for every_sequence_name in list_of_names_of_all_sequences:
            if every_sequence_name[x] in char_check:
                pass
            else:
                char_check.append(every_sequence_name[x])

        if len(char_check) == 1:
            char_to_be_removed_counter += 1


# --------------------------------------------------------------
# Creating the output file 06_sequence_with_domains.fasta
# It contains the protein target (the one with SP if deepsig has been used, otherwise all protein inside the fasta source) and they sequence extracted

root = fastasource.replace(".fasta", "")

with open(fastasource, "r") as file_fasta:
    for record in SeqIO.parse(file_fasta, "fasta"):
        for everyelement in dict_seq:
            if dict_seq[everyelement][0] == record.id:
                dict_seq[everyelement].append(record.seq)
		# {0: ['Proteinasuper', 'vwA_MSA', 'empty', '658', '827', Seq('RECLCGALASYAAACAGRGVRVAWREPGRCELNCPKGQVYLQCGTPCNLTCRSL...CSK')], ...}

seq_already_written = []


with open(f"{output_path}/06_sequences_which_have_domains.fasta", "w") as extraction_part1:
    pass
with open(f"{output_path}/06_sequences_which_have_domains.fasta", "a") as extraction_part2:
    for everyelement in dict_seq:
        if dict_seq[everyelement][0] in seq_already_written:
            pass
        else:
            extraction_part2.write(
                f">{root}_{dict_seq[everyelement][0][char_to_be_removed_counter:]}\n{dict_seq[everyelement][5]}\n\n")
		# >Hsapiens_VWF_Proteinasuper
		# RECLCGALASYAAACAGRGVRVAWREPGRC.....
            seq_already_written.append(dict_seq[everyelement][0])

print_message(file_06)

# --------------------------------------------------------------
# Creating the output file 07_extracted_domains.fasta
# Extracing all the domains found inside the target in a single file

with open(f"{output_path}/07_extracted_domains.fasta", "a") as extraction_part3:

    for everyelement in dict_seq:
        domain = str(dict_seq[everyelement][5])
        extraction_part3.write(
            f">{root}_{dict_seq[everyelement][0][char_to_be_removed_counter:]}-{dict_seq[everyelement][1]}-from{dict_seq[everyelement][3]}to{dict_seq[everyelement][4]}\n{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n")

print_message(file_07)

# --------------------------------------------------------------
# Creating the output file 08_extracted_domains.csv
# Extracing all the domains found inside the target in a single file

with open(f"{output_path}/08_extracted_domains.csv", "a") as extraction_part4:
    header_string = "Fasta file,sequence name,domain name,length,aa coords,sequence\n"
    extraction_part4.write(header_string)

    for everyelement in dict_seq:
        domain = str(dict_seq[everyelement][5])
        domain_length = int(dict_seq[everyelement][4]) - int(dict_seq[everyelement][3])
        extraction_part4.write(f"{root},{dict_seq[everyelement][0][char_to_be_removed_counter:]},{dict_seq[everyelement][1]},{domain_length},{dict_seq[everyelement][3]}-{dict_seq[everyelement][4]},{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n")

print_message(file_08)


# --------------------------------------------------------------
# Creating the output file extracted_domains_from_ALL_targets.fasta
# Combining all the domains found from ALL the target in a single fail

with open("../tmp_folder/all_extracted_domains", "r") as newfile:
    one_file = newfile.read().strip()
    if one_file == "1":
	    with open("all_extracted_domains.fasta", "a") as commmonfile: 
            for everyelement in dict_seq:
                domain = str(dict_seq[everyelement][5])
                commmonfile.write(f">{root}_{dict_seq[everyelement][0][char_to_be_removed_counter:]}-{dict_seq[everyelement][1]}-from{dict_seq[everyelement][3]}to{dict_seq[everyelement][4]}\n{domain[int(dict_seq[everyelement][3]):int(dict_seq[everyelement][4])]}\n\n")


# --------------------------------------------------------------
# Creating the final report
# How many domains have been found per sequence?

# Filtering for the columns of interest
df_selected2 = df[["query_name"]]

listofvalues = df_selected2.values

unique_domains_found = []
domains_found_dict = {}

for x in listofvalues:
	if x[0] in unique_domains_found:
		domains_found_dict[x[0]] += 1
	else:
		unique_domains_found.append(x[0])
		domains_found_dict[x[0]] = 1

domains_found_dict_sorted = dict(sorted(domains_found_dict.items(), key=lambda item: item[1], reverse=True))

with open(f"{output_path}/09_domains_found.csv", "w") as domains_found_file:
	linetowrite = ""
	for everyitem in domains_found_dict_sorted:
		linetowrite += f"{everyitem}, {domains_found_dict_sorted[everyitem]}\n"
	domains_found_file.write(linetowrite)
	
print_message(file_09)

