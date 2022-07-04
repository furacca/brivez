# How to download the full Pfam database
If you want to download the entire Pfam database (~1.6 GB, extracted)
1) The file of our interest is `Pfam-A.hmm`
2) In your download folder open a terminal and type
   - `ftp ftp://ftp.ebi.ac.uk/`
   - `cd pub`
   - `cd databases`
   - `cd Pfam`
   - `cd current_release`
   - `get Pfam-A.hmm.gz`
   - `get md5_checksums`
   - `exit`
   - `md5sum --check md5_checksum`
   - `gzip -d Pfam-A.hmm.gz`
3) Copy your file inside the `00_hmm_profile_target` folder of Brivez
4) Done. 


# How to download a specific ~.hmm file
1) Go to https://pfam.xfam.org/
2) Click on the section "SEARCH" in the top menu
3) Click on the section "Domain architecture" in the left menu
4) Type the domain's name that are you looking for (i.e. PF00092 or vWA) and click "Go"
5) Click on the relative accession
6) In the left menu (inside the tab of PF00092) select "Alignments"
7) Under the voice "Format an alignment" choise the seed or full alignment, format selex and click generete 
8) Copy your file inside the `00_hmm_profile_target` folder of Brivez
9) Done. 
