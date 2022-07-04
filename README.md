# Brivez - beta 0.1
Brivez is a bioinformatic tool which if provided with single/multiple transcriptome.fasta file and profile.hmm domain it returns all the domains found in a single file.fasta (of course there are more in the readme).

**At the moment this program run exclusively on Linux (tested on Debian 11 and Ubuntu 22.04).**

All the software used are OpenSource.<br>
**Total memory used**: ~3.5 GB.<br>
**Multi-core CPU** is suggested.<br>
**SSD** is suggested.<br>
<br>
<br>
## Index ##
- [Suggested use](#suggested-use)<br>
- [Software requirements](#software-requirements)<br>
- [Quickly set up](#quickly-set-up)<br>
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

1) **Quick install for [Conda](https://docs.conda.io/en/latest/)** (following the online doc is suggested):
   1) Download the installer at this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
   2) Verify your installer hashes
   3) In the terminal run `bash Anaconda-latest-Linux-x86_64.sh`. 
   Now in your terminal you will see something like `(base) user@host:~$`: the `base` indicates the name of the active environment.  It's possible to create an enviroment _ad hoc_ running in the terminal: `conda create - n name_of_the_environment`. To see all the env use `conda env list`.
   4) Choose the enviroment with `conda activate name_of_the_environment` (`conda deactivate [...]` to close the active environment)
2) **Install in Conda some stuff:**
   1) conda config --add channels bioconda
   2) conda install pandas
   3) conda install -c bioconda samtools
   4) conda install -c conda-forge dpath
3) **Install the predictor of signal peptides, [**DeepSig**](https://github.com/BolognaBiocomp/deepsig)**
    1) Just as described on its site `conda install -c bioconda deepsig`

4) **Install [HMMER3](http://hmmer.org/)**
   1) `sudo apt-get install hmmer` (v3.3.2 both on Ubuntu 22.04 and Debian 11)


# Future updates

**TOP PRIORITY**
- None

**MEDIUM PRIORITY**
- Extracted list of all SP (008_*.fa maybe?)

**LOW PRIORITY**
- Check some solution for Mac and Windows 10 - 11(W. subsystem for Linux)
