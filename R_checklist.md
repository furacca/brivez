# CHECKLIST!
I love checklist.

## Checklist - BEFORE running Brivez
1) For every folder there is one and only one list of sequence/transcriptome
2) The list of sequence/transcriptomes are in .fasta file (no .fa, .fas, ecc)
3) In the root you have:
   - 00_hmm_profile_target folder with inside ONE ~.hmm file
   - 00_script folder with inside FOUR script
   - Research_number_X_OUTPUT-FOLDER, where X is a number > 0
   - One folder per one transcriptome
4) Check to have the right environment activated (`conda activate therightenvironment`)
5) Have fun!


## Checklist - ERRORS EVERYWHERE!
1) Keep calm
2) Save all the data in Research_number_X_OUTPUT-FOLDER that you need
4) Run `./wipe_all.sh iamsureofthis` (be really sure) which: <br>
   - Delete every Research_number_X_OUTPUT-FOLDER
   - Delete the log file
   - Delete every accessory file EVERYWHERE inside the root
   - Check the name of the essential file
5) Check that for every sequence's list you have just one folder
6) Check that the sequence's list is in .fasta format
7) Check to have the right environment activated (`conda activate therightenvironment`)
8) If all is useless, report it on the github section
9) Delete the folder (`rm -r ./bravez/*` if you are brave enough)
10) Redownlaod the project (for exemple with `git clone https://github.com/furacca/bravez`)
11) Follow the "BEFORE running Brivez" checklist