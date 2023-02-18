# HMMER tool in more details

**Official HMMER User's Guide**<br>
http://eddylab.org/software/hmmer/Userguide.pdf

---


Brivez run hmmsearch as the following:<br>
`hmmsearch --domtblout table.output -E 1e-5 --domE 1e-5 --cpu 2 hmmfile target.fastsa`<br>

This line **can be edited** at **line 95** inside `brivez_man.sh`. 

- `-E 1e-5`
<br> Report target sequences with an E-value of <= X. The default is 10.0 ([read p. 104](http://eddylab.org/software/hmmer/Userguide.pdf)).
- `--domE 1e-5`
<br> For target sequences that have already satisfied the per-profile reporting threshold, report individual domains with a conditional E-value of <= X. The default is 10.0 ([read p. 104](http://eddylab.org/software/hmmer/Userguide.pdf)).
- `--cpu 6`
<br> Set the number of parallel worker threads to N. On multicore machines, the defaults is two. Can be use also --mpi in alternative ([read p. 107](http://eddylab.org/software/hmmer/Userguide.pdf)).


From the table.output are extracted two kind of coordinates:
- `ali coord`
<br> The start of the [MEA](#useful-things-to-know) alignment of this domain with respect to the sequence ([read p. 72](http://eddylab.org/software/hmmer/Userguide.pdf))
- `env coord`
<br> The start and the end of the domain envelope on the sequence. ([read p. 72](http://eddylab.org/software/hmmer/Userguide.pdf))

**By default, Brivez use the env coord**, but it's possible to **change it** on line 43 in ./00_script/brivez_script02.py:
- change `df_selected = df[["target_name", "query_name", "accession1", "START_ali", "END_ali"]]` <br>
- with `df_selected = df[["target_name", "query_name", "accession1", "START_envelope", "END_envelope"]]`
<br>

#### Useful things to know:
- `hmmpress` is useful only if used with `hmmscan` ([read p. 97](http://eddylab.org/software/hmmer/Userguide.pdf))
- `MEA` Maximum Expected Accuracy
- `envelope` When HMMER identifies domains, it identifies what it calls an envelope bounding where the domain’s alignment most probably lies. The envelope is almost always a little wider than what HMMER chooses to show as a
reasonably confident alignment.