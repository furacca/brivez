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
#  PREPARATION
##########################################################

echo "------ PREPARATIONS -------"
echo ""
# Folder check
echo "[] Folder check"
folder_found=( $(find . -mindepth 1 -maxdepth 1 -type d ! -path "./Research_number_*" ! -path "./00_hmm_profile_target" ! -path "./.*" ! -path "./00_script" ! -path "./.*" ) )
echo "	*** Have been found ${#folder_found[@]} target folder ***"
for everyfolder in ${folder_found[@]}; do
	echo "	--> $everyfolder"
done
echo "$target_folder_found"

# Log check
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

# hmm file check
echo "[] HMM file check"
HMM_FILE=( $(ls ./00_hmm_profile_target) )
echo "	In this analysis will be used $HMM_FILE file"
echo ""


# OUTPUT FOLDER CREATION
echo "[] Organizing the output folder"
mkdir "$folder_name"
echo "	The output folder $folder_name has been created."
cd $folder_name
touch 001_all_sequences_extracted.fasta
echo "		--> Created 001_all_sequences_extracted.fasta file in the folder"
touch 002_all_domains_extracted.fasta
cd ..
echo "		--> Created 002_all_domains_extracted.fasta file in the folder"
echo ""

##########################################################
# ---- ANALYSIS TIME -----
##########################################################
for everyfolder in ${folder_found[@]}; do
	target_folder=( $(echo $everyfolder) )
	for everyelement2 in ${target_folder[@]}; do
		cd $folder_name
		mkdir $everyelement2
		cd ..
		cd $everyelement2
		trascrittoma=( $(find . -type f -name "*.fasta") )
		echo "------ STARTING THE ANALYSIS FOR THE $everyelement2 FOLDER -------"
		echo ""
		echo "[] Deepsig"
		deepsig -f ./$trascrittoma -o 001_deepsig_output.tsv -k euk
		cp ../00_script/brivez_script01.py ./brivez_script01.py
		echo "[] Executing the ./script01.py"
		./brivez_script01.py
		rm ./brivez_script01.py
		echo "[] Executing hmmsearch"

#		This line is editable
		hmmsearch --domtblout 003_hmmer_output_table -E 1e-5 --domE 1e-5 --cpu 6 ../00_hmm_profile_target/$HMM_FILE ./002_deepsig_sequence_with_SP.fa > /dev/null

		cp ../00_script/brivez_script02.py ./brivez_script02.py
		echo "[] Executing the ./script02.py"
		./brivez_script02.py
		rm ./brivez_script02.py
		mv ./001_deepsig_output.tsv ../$folder_name/"$everyelement2"/001_deepsig_output.tsv
		mv ./002_deepsig_sequence_with_SP.fa ../$folder_name/"$everyelement2"/002_deepsig_sequence_with_SP
		mv ./003_hmmer_output_table ../$folder_name/"$everyelement2"/003_hmmer_output_table
		mv ./004_hmmer_output_table_data_parsed ../$folder_name/"$everyelement2"/004_hmmer_output_table_data_parsed
		mv ./005_pandas_sequences_table.tsv ../$folder_name/"$everyelement2"/005_pandas_sequences_table.tsv
		mv ./006_sequence_with_SP+Domain_extracted.fa ../$folder_name/"$everyelement2"/006_sequence_with_SP+Domain_extracted.fa
		mv ./007_domains_of_sequences_with_SP+Domain_extracted.fa ../$folder_name/"$everyelement2"/007_domains_of_sequences_with_SP+Domain_extracted.fa
		mv ./008_domains_found.csv ../$folder_name/"$everyelement2"/008_domains_found.csv
		mv ./009_domains_found_seaborn_plot.png ../$folder_name/"$everyelement2"/009_domains_found_seaborn_plot.png
		cd ..
	done
done


# # ---- CONGRATULATION TIME -----
echo ""
echo "------ CONGRATULATIONS -------"
echo ""
echo "The operation has gone well (or I've missed the bug)."
echo "Have a good day"
echo ""
