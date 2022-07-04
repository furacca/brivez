#!/bin/bash
##########################################################
# A Welcome art, indeed useful
##########################################################

echo ""
echo "  ____  _____  _______      ________ ______"
echo " |  _ \|  __ \|_   _\ \    / /  ____|___  /"
echo " | |_) | |__) | | |  \ \  / /| |__     / / "
echo " |  _ <|  _  /  | |   \ \/ / |  __|   / /  "
echo " | |_) | | \ \ _| |_   \  /  | |____ / /__ "
echo " |____/|_|  \_\_____|   \/   |______/_____|"
echo ""
echo ""
echo "Bioinformatic tool - https://github.com/furacca/brivez"

##########################################################

echo "------ PREPARATIONS -------"
echo ""

# FOLDER CHECK
echo "[] Folder check"
folder_found=( $(find . -mindepth 1 -maxdepth 1 -type d ! -path "./Research_number_*" ! -path "./hmm_profile_target*" ! -path "./.*") )
echo "	*** Have been found ${#folder_found[@]} target folder ***"

for everyfolder in ${folder_found[@]}; do
	echo "	--> $everyfolder"
done

echo "$target_folder_found"

# LOG CHECK
echo "[] Log check"
FILE=./log
if [ -f "$FILE" ];then
	echo "	Log exists"
	log_counter=($(cat log))
	echo "$((log_counter + 1))" > log
	folder_name="Research_number_$((log_counter + 1))_OUTPUT-FOLDER"
else
	echo "	Pre-existent log not found"
	touch log
	echo "1" > log
	echo "	New log file created"
	folder_name="Research_number_1_OUTPUT-FOLDER"
fi
echo ""

# HMM FILE CHECK
echo "[] HMM file check"
HMM_FILE=( $(ls ./hmm_profile_target) )
echo "	In this analysis will be used $HMM_FILE file"
echo ""


# OUTPUT FOLDER CREATION
echo "[] Organizing the output folder"
mkdir "$folder_name"
echo "	The output folder $folder_name has been created. It contains two output file:"
cd $folder_name
touch 001_all_sequences_extracted.fasta
echo "		--> Created 001_all_sequences_extracted.fasta file in the folder"
touch 002_all_domains_extracted.fasta
cd ..
echo "		--> Created 002_all_domains_extracted.fasta file in the folder"
echo ""

# ANALYSIS TIME
for everyelement in ${folder_found[@]}; do
	arrayxyz=( $(echo $everyelement) )
	for everyelement2 in ${arrayxyz[@]}; do
		cd $everyelement2
		trascrittoma=( $(ls) )
		echo "------ STARTING THE ANALYSIS FOR THE $everyelement2 FOLDER -------"
		echo ""
		echo "[] Deepsig"
		deepsig -f ./$trascrittoma -o 001_deepsig_output.tsv -k euk
		cp ../brivez_script01.py ./brivez_script01.py
		echo "[] Executing the ./script01.py"
		./brivez_script01.py
		rm ./brivez_script01.py
		echo "[] Executing hmmsearch"
		hmmsearch --domtblout 003_hmmer_output_table -E 1e-5 --domE 1e-5 --cpu 10 ../hmm_profile_target/$HMM_FILE ./002_deepsig_sequence_with_SP.fa > /dev/null
		cp ../brivez_script02.py ./brivez_script02.py
		echo "[] Executing the ./script02.py"
		./brivez_script02.py
		rm ./brivez_script02.py
#		# 001_deepsig_output.tsv
#		# 002_deepsig_sequence_with_SP.fa.fasta
#		# 003_hmmer_output_table
#		# 004_hmmer_output_table_data_parsed.fasta
#		# 005_pandas_sequences_table.tsv
#		# 006_sequence_with_SP+Domain_extracted.fa
#		# 007_domains_of_sequences_with_SP+Domain_extracted.fa
		cd ..
	done
done

# CONGRATULATIONS
echo ""
echo "------ CONGRATULATIONS -------"
echo ""
echo "The operation has gone well (or I've missed the bug)."
echo "Have a good day"
echo ""



