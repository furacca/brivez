<p align="center"><img src="./logo.png"></p>

Brivez is a bioinformatic tool which if provided with single/multiple transcriptome.fasta file and profile.hmm domain it returns all the domains found in a single file.fasta (of course there are more in the readme).

**At the moment this program run exclusively on Linux (tested on Debian 11 and Ubuntu 22.04).**

All the software used are OpenSource.<br>
**Total memory used**: ~3.5 GB.<br>
**Multi-core CPU** is suggested.<br>
**SSD** is suggested.<br>
<br>
<br>
# Index #
- [Suggested use](#suggested-use)<br>
- [Software requirements](#software-requirements)<br>
- [Quickly set up](#quickly-set-up)<br>
- [First run and checklist](#first-run-and-checklist)<br>
- [Avoid the following](#Avoid-the-following)<br>
- [Future updates](#future-updates)<br>

# Suggested use
Brivez is a bioinformatic tool which has been thought as Quality of Life's improvement.
Its main goal is to extract all the domains sequence inside the proteins, given a sequence target (proteins list or transciprome) and a ~.hmm profile.


# Software requirements
Long list short:
- Conda (~minimum 3 GB)
- Environment inside Conda with:
  - Deepsig (~50 MB)
  - Pandas (~15 MB)
  - Bioconda 
  - fnmatch (samtools -~1 MB)
- HMMER3 v3.3.2 (~ 20 MB)

# Quickly set up

**01 - Quick install for [Conda](https://docs.conda.io/en/latest/)** (following the online doc is suggested):
   1) Download the installer at this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
   2) Verify your installer hashes
   3) In the terminal run `bash Anaconda-latest-Linux-x86_64.sh`. 
   Now in your terminal you will see something like `(base) user@host:~$`: the `base` indicates the name of the active environment.  It's possible to create an enviroment _ad hoc_ running in the terminal: `conda create - n name_of_the_environment`. To see all the env use `conda env list`.
   4) Choose the enviroment with `conda activate name_of_the_environment` (`conda deactivate [...]` to close the active environment).

**02 - Install in Conda some stuff:**<br>
   1) conda config --add channels bioconda
   2) conda install pandas
   3) conda install -c bioconda samtools
   4) conda install -c conda-forge dpath

**03 - Install the predictor of signal peptides, [**DeepSig**](https://github.com/BolognaBiocomp/deepsig)**<br>
   1) Just as described on its site, use <br>`conda install -c bioconda deepsig`

**04 - Install [HMMER3](http://hmmer.org/)**<br>
   1) Just as described on its site, use<br>`sudo apt-get install hmmer` (v3.3.2 both on Ubuntu 22.04 and Debian 11)

**05 - Downlaod Brivez**<br>
   1) Download the Brivez folder with<br>
`git clone https://github.com/furacca/bravez`
or whatever way you prefer

# First run and checklist

BEFORE ever thinking of runninng Brivez you MUST:<br><br>
**01 - GIVE PERMISSIONS TO SCRIPTS**<br>
- Inside your folder type `chmod +x ./00_script/TOOL_chmod_the_scripts.sh && ./00_script/TOOL_chmod_the_scripts.sh`. <br>
Now all the script files can see their job done.

**02 - ONE FOLDER PER ONE SEQUENCE'S LIST / TRASCRIPTOME**<br>
1) Create a folder (if you have multiple transcriptome, using the organism's name could be a great thing)
2) Put your sequence's list inside the folder, **using the .fasta format** (no .fas, .fa, ..)
3) Keep the ratio **1 transcriptome : 1 folder**

**03 - OPTIONAL - REMOVE ALL THE ASTERISKS FROM FASTA FILE**<br>
- Consider to remove all the asterisks from all your fasta file, with:<br>
`./00_script/TOOL_remove_asterisk_From_fasta_file`<br>
This wil be overwrite the original file.

**03 - ONE HMM FILE INSIDE 00_hmm_profile_target**<br>
- Download from [Pfam](https://pfam.xfam.org/) the hmm file that you are going to use (maybe can be helpfull follow [the following guide](https://github.com/furacca/brivez/blob/main/README_Pfam_database.md)).

**04 - OPTIONMAL - CHECKLIST**<br>
- Follow this [checklist](https://github.com/furacca/brivez/blob/main/README_checklist.md) to be sure that everything's ok.

**05 - RUN BRIVEZ**<br>
- In the root of the Brivez folder type in the terminal:<br>
`./brivez_main.sh`

**06 - CLEAN UP THE WORKSPACE**<br>
- Delete every output folder created and the log file with<br>
`./wipe_all.sh`

# Avoid the following 
1) DO NOT CHANGE/RENAME/MOVE ANY FOLDER/FILE, unless is something that you have add.


# Future updates

**TOP PRIORITY**
- Reorganizing commenting for all the code
- Output file ready to be elaborated with Muscle/TCoffee and MrBayes

**MEDIUM PRIORITY**
- Extracted list of all SP (008_*.fa maybe?)
- Create checkpoint to have multiple feedbacks while the program is ongoing (and create a REPORT!)

**LOW PRIORITY**
- Check some solution for Mac and Windows 10 - 11(W. subsystem for Linux)
- Possibility to disable Deepsig (sequences already selected or something else)
- Choose multiple domains 
