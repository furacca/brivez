#!/bin/bash

# Running a MSA alignment

FILE=./log
log_counter=($(cat log))
folder_name="Research_number_$((log_counter))_OUTPUT-FOLDER"

echo "$folder_name"

echo ""
echo "------ STARTING THE MUSCLE ANALYSIS INSIDE $folder_name -------"
cd $folder_name
echo "	Runing MUSCLE"
muscle -align 002_all_domains_extracted.fasta -output 002_msa_muscle.fasta
echo "  --> Done"