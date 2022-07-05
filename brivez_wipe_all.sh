#!/bin/bash
##########################################################
# Thanks http://www.geocities.ws/SoHo/7373/cloth.html#toilets for the paper's ASCII art
##########################################################
# The secret agreement work is "iamsureofthis". Shhhhhh!
##########################################################

echo ""
echo "                                               _....._                   "
echo " __        _____ ____ ___ _   _  ____         ;.__-__.;-._               "
echo " \ \      / /_ _|  _ \_ _| \ | |/ ___|        |       |   :-.__ .-;      "
echo "  \ \ /\ / / | || |_) | ||  \| | |  _         |       |   :    :  |      "
echo "   \ V  V /  | ||  __/| || |\  | |_| |        |       |   :    :  |      "
echo "    \_/\_/  |___|_|  |___|_| \_|\____|        '._____.'-._:    :  |      "
echo "                                                           -.__;.-'      "

if [ "$1" == "iamsureofthis" ]; then
  echo ""
  echo "------ STARTING -------"
  echo ""
  echo "[] Wiping check"
  folder_found=( $(find . -mindepth 1 -maxdepth 1 -type d ! -path "./Research_number_*" ! -path "./hmm_profile_target*" ! -path "./.*") )
  echo "  Wiping all the output folders:"
  rm -rf ./Research_number_*
  echo "  --> Done"
  echo "  Wiping the log file:"
  rm -f ./log
  echo "  --> Done"
  echo "  Wiping all the accessory files:"
  find . -type f -name "001_deepsig_output.tsv" -delete
  find . -type f -name "002_deepsig_sequence_with_SP.fa" -delete
  find . -type f -name "003_hmmer_output_table" -delete
  find . -type f -name "004_hmmer_output_table_data_parsed" -delete
  find . -type f -name "005_pandas_sequences_table.tsv" -delete
  find . -type f -name "006_sequence_with_SP+Domain_extracted.fa" -delete
  find . -type f -name "007_domains_of_sequences_with_SP+Domain_extracted.fa" -delete
  find . -type d -name "job.tmpd.*" -delete
  echo "  --> Done"
  echo ""
  echo "  All the files and folder have been wiped out."
  echo ""
  echo ""
  echo "[] Folder's name check"
  hmm_folder_check=( $(find . -type d -path "./00_hmm_profile_target") )
  script=( $(find . -type d -path "./00_script") )
#   Rewrite it with -case- ?
  if [ "$hmm_folder_check" == "./00_hmm_profile_target" ]; then
    if [ "$script" == "./00_script" ]; then
      echo "  ---> Done"
    else
      echo " ---------------------- WARNING! --------------------- "
      echo "The name of ./00_script is changed. Please, check it."
      exit
    fi
  else
    echo " ---------------------- WARNING! --------------------- "
    echo "The name of ./00_hmm_profile_target is changed. Please, check it."
    exit
  fi
  echo ""
  echo ""

else
  echo ""
  echo " ---------------------- WARNING! --------------------- "
  echo "The secret agreement word to delete everything is wrong."
  echo "A mistake, maybe?"
  echo "-------------------------------------------------------"
  echo ""
  exit
fi
echo "---> EVERYTHING SEEMS TO BE ALRIGHT, but I am a mere script"
echo ""
echo "Have fun!"
echo ""
