#!/bin/bash
# coding: utf-8

# --------------------------------------------------------------
# A Welcome art, indeed useful

echo ""
echo "  ____  _____  _______      ________ ______"
echo " |  _ \|  __ \|_   _\ \    / /  ____|___  /"
echo " | |_) | |__) | | |  \ \  / /| |__     / / "
echo " |  _ <|  _  /  | |   \ \/ / |  __|   / /  "
echo " | |_) | | \ \ _| |_   \  /  | |____ / /__ "
echo " |____/|_|  \_\_____|   \/   |______/_____|"
echo ""
echo ""
echo "Brivez is a bioinformatic tool thought as Quality of Life's improvement, providing high quantity of data in a snap, giving you a quick view on what you could find inside your sequences' list"
echo ""
echo "More info here: https://github.com/furacca/brivez"
echo ""
echo ""

# --------------------------------------------------------------
# Defining some functions

# Function called if you run the bash with -h option
Help()
{
   echo "############################################"
   echo ""
   echo "HELP MENU"
   echo "	"
   echo "Syntax: "
   echo "brivez_main.sh [-h|-b|-a]"
   echo "	options:"
   echo "	-h	print this help message."
   echo "	-a	deepsig will not be used; all sequences will be scanned"
   echo "	-b	create an additional file which contains the results from ALL scans"
   echo "	"
   echo "############################################"
   echo ""
}


# --------------------------------------------------------------
# ---- PRE-PREPARATION -----
# Setting up some variables

# Default: 0 (false)
skipdeepsig=1

# Change this variable on the base of how many thread do you have
# (Keep in mind that disk r/o speed >>>>> cores' number)
hmmercpu=4

# Delete the previously temporary folder and recreate a new temporary folder
rm -f -r tmp_folder && mkdir tmp_folder

# By default the creation of one file with the extracted domains from ALL fasta target is DISABLED
echo "0" > tmp_folder/all_extracted_domains
all_extracted_domains="0"

# Read the option given to this script
while getopts "hab" option; do
   case $option in
         h) # Help
         Help
         exit;;
         a) # Skip deepsig
         skipdeepsig=0
         #modechoosen="Deepsig skipped"
         ;;
         b) # Create one file with the extracted domains from ALL fasta target
         echo "1" > tmp_folder/all_extracted_domains
         all_extracted_domains="1"
         ;;
        \?) # Invalid option
	 echo "Use -h option to get some hint on the usage of this software"
	 echo ""
         exit;;
   esac
done


# --------------------------------------------------------------
# ---- PREPARATION -----

echo ""
echo "-------------------------------------------------------------------"
echo "------ PHASE 1 - PREPARATIONS -------------------------------------"
echo "-------------------------------------------------------------------"
echo ""

# Fasta files taget check
echo "    [] Found the following fasta files:"
find ./02_fasta_target -name '*.fasta' | while read LINE; do echo "	-->  $LINE" ; done

# Log check
echo "    [] Log check"
FILE=./.research_number
if [ -f "$FILE" ];then
	echo "	Log exists"
	log_counter=($(cat .research_number))
	echo "$((log_counter + 1))" > .research_number
	echo "	This is the experiment number $((log_counter + 1))"
	folder_name="Research_number_$((log_counter + 1))"
else
	echo "	Pre-existent log not found"
	touch .research_number
	echo "1" > .research_number
	echo "	New log file created"
	folder_name="Research_number_1"
fi

# HMM file check
echo "    [] HMM file check"
HMM_FILE_FOUND=( $(find ./01_hmm_profiles -name "*.hmm" | wc -w) )
if [ $HMM_FILE_FOUND -eq 1 ];then
	HMM_FILE=( $(ls ./01_hmm_profiles) )
	echo "	This analysis will use the following hmm file:"
	echo "		$HMM_FILE"
else
	echo "	The following hmm files have been found:"
	for f in $(ls ./01_hmm_profiles); do
		echo "		$f"
	done
	cd ./01_hmm_profiles
	read -e -p "	Choose one hmm file for this analysis : " hmmchoice
	HMM_FILE=$hmmchoice
	echo "	$hmmchoice will be used in this run."
	cd ..
fi


# Output folder creation
echo "    [] Creating the output folder"
mkdir "$folder_name"
echo "	The output folder $folder_name has been created."
echo ""
echo ""


# CHECKING IF THERE IS ANY FILE(S) WITH A SPACE IN ITS NAME
# Checking the space and not coping all the dir' files is more disk space friendly
echo "-------------------------------------------------------------------"
echo "------  PHASE 2 - REMOVING ALL THE SPACES FROM FILE(S) NAME -------"
echo "-------------------------------------------------------------------"
echo ""
cd 02_fasta_target
# Hiding the output of ls
ls | grep " " 1>/dev/null
# If the exit code is 0 (grep " " has found something)
if [ $? -eq 0 ] 
then
	echo "	SPACE DETECTED ! ! !"
	echo "	[] All the spaces inside the names of the 02_fasta_target dir will be changed in underscore _"
	while true; do
	read -p "	Do you want to proceed? The file will be renamed. (yes/no) " yn
	case $yn in 
		yes ) echo "	Done";
			break;;
		y ) echo "	Done";
			break;;
		no ) echo "	Exiting";
			exit;;
		n ) echo "	Exiting";
			exit;;
		* ) echo "	Invalid response" && echo "";;
	esac
	done
else
	echo "    [] It seems that all the file(s) names are ok."
fi

for file in *; do mv "$file" `echo $file | tr ' ' '_'`; done 2>/dev/null

echo ""
echo ""

# --------------------------------------------------------------
# ---- ANALYSIS TIME -----

# Keeping track of the time
# https://www.xmodulo.com/measure-elapsed-time-bash.html

start_time=$SECONDS

echo "-------------------------------------------------------------------"
echo "------  PHASE 3 - ANALYSIS ----------------------------------------"
echo "-------------------------------------------------------------------"
echo ""

# Euk, gram+, gram-"
organism="euk"

#Final report counter
fastafilesfound=0

# Copying the scripts inside the working dir (they will be deleted at the end of the analysis)
cp ../00_script/brivez_script01.py .
cp ../00_script/brivez_script02.py .

# Analyzing every file
# It is useful while you need to analyze multiple files at the same time
for file in $(ls *.fasta); do
	
	# Update counter
	fastafilesfound=$(( fastafilesfound + 1 ))

	# Removing ".fastas" from the file's name
	filenameroot=${file:0:-6}
	
	# Create a temporary output folder
	mkdir tmp_output
	
	# Banner for this file
	echo "============= $file ============="
	
	# Deepsig part
	if [ $skipdeepsig -eq 1 ];
	then
		echo "===== Deepsig"
		deepsig -f ./$file -o ./tmp_output/01_deepsig-analysis.tsv -k $organism
		echo "Created -------->    01_deepsig-analysis.tsv"
	else
		echo "===== Skipped Deepsig"
		echo "i	am	not	the	one	who	you	think" > ./tmp_output/01_deepsig-analysis.tsv
		echo "Created -------->    01_deepsig-analysis.tsv (mock file)"
	fi
	
	
	# File used by brivez_script01.py to extract the rootname of the fastas' source
	# It simply deletes ROTFLMAO from the name
	touch "ROTFLMAO$file"
	
	# Selecting sequences part
	echo "===== Selecting fasta's sequences"
	echo "Success"
	python3 brivez_script01.py
	
	# hmmsearch part
	echo "===== HMMsearch"
	# This line is editable
	# In the future this will be changed, using variables to highlight the editable settings
	hmmsearch --domtblout tmp_output/03_hmmsearch_output_table -E 1e-5 --domE 1e-5 --cpu $hmmercpu ../01_hmm_profiles/$HMM_FILE tmp_output/02_sequences_selected.fasta >/dev/null
	if [ $? -eq 0 ] 
	then
		echo "Success"
		echo "Created -------->    03_hmmsearch_output_table"
	else
		echo "HMMsearch have encountered some problem."
	fi

	# Analysis part
	echo "===== Analyzing the result"
	python3 brivez_script02.py

	# Partial cleaning phase
	rm ROTFLMAO$file
	mv tmp_output ../$folder_name/$filenameroot
	echo ""
	echo ""
	echo ""
	echo ""
done


# --------------------------------------------------------------
# ---- CONGRATULATION TIME -----

# Check out how much time has passed
elapsed=$(( SECONDS - start_time ))

# Todays date
todaysdate=$(date +"%F")

# Domains found
# Next update? 
#domainsfound=1

echo "-------------------------------------------------------------------"
echo "------ PHASE 4 - REPORT -------------------------------------------"
echo "-------------------------------------------------------------------"



echo ""
# Date
echo "Todays date:				$todaysdate" && echo "Todays date:				$todaysdate" > Report
# Output folder name
echo "Output fodler's name:			$folder_name" && echo "Output fodler's name:			$folder_name" >> Report
# Option a enabled
texttoinsert_0="Skip deepsig"
if [ $skipdeepsig -eq 0 ];then echo "Option selected: 			$texttoinsert_0" && echo "Option selected: 			$texttoinsert_0" >> Report;fi
# Option b enabled
texttoinsert_1="ALL results from scans in one file" 
if [ $all_extracted_domains -eq 1 ];then echo "Option selected: 			$texttoinsert_1" && echo "Option selected: 			$texttoinsert_1" >> Report;fi
# Number of FASTA files analyzed
echo "FASTA file(s) found and analyzed: 	$fastafilesfound" && echo "FASTA file(s) found and analyzed*: 	$fastafilesfound" >> Report
# HMM file used
echo "HMM profile used:			$HMM_FILE" && echo "HMM profile used:			$HMM_FILE" >> Report
# domain found with HMM analysis (next update?)
#echo "Domains found with this HMM profile:	$domainsfound" && echo "Domains found with this HMM profile:	$domainsfound" >> Report
# Analysis duration
echo "Analysis duration:			$elapsed seconds" && echo "Analysis duration:			$elapsed seconds" >> Report
echo ""


# Info not displayed - only for the written report
echo "" >> Report
echo "" >> Report
echo "" >> Report
echo "*Fasta file(s) analyzed:" >> Report
for file in $(ls *.fasta); do
	echo "	$file" >> Report
done


# Final message
echo ""
echo "To see the output folder:"
echo "cd 03_results/$folder_name"
echo ""

# # ---- CLEANING TIME -----

# Move the Report inside the results folder
mv Report ../$folder_name/

# Check if -b option is activated; if yes, do things
if [ $all_extracted_domains -eq 1 ];then
	mv all_extracted_domains.fasta ../$folder_name 
fi


# Move this research inside the results folder
mv ../$folder_name ../03_results/


rm brivez_script01.py
rm brivez_script02.py
rm -r ../tmp_folder



