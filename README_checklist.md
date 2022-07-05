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
2) Check that for every sequence's list you have just one folder
3) Check that the sequence's list is in .fasta format
4) Check to have the right environment activated (`conda activate therightenvironment`)

-- *music intensifies* - Entering the serious mode --

7) Backup the data that you want to save (maybe some Research_number_X_OUTPUT-FOLDER?)
8) Run `./brivez_wipe_all.sh iamsureofthis` (be really sure) which will: <br>
   - Delete every Research_number_X_OUTPUT-FOLDER
   - Delete the log file
   - Delete every accessory file EVERYWHERE inside the root
   - Check the name of the essential file

9) If all is useless, report it on the GitHub section (be detailed, please)
10) Delete the folder (`rm -r ./brivez/*`)
11) Download again the project (for example with `git clone https://github.com/furacca/bravez`)
12) Follow the "BEFORE running Brivez" checklist