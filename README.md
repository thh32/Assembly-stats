# Assembly-stats
Provides some of the common assembly statistics used to identify how good a metagenomic assembly is.


##Statistics  
-N50
-Total bases in assembly
-Longest contig
-Smallest contig


A plot of the contigs lengths within the assembly is also produced and labelled using the `-o` option



##Usage

Use Assembly_stats.py like so;
```
python Assembly_stats.py -fasta -i $INPUT -o $OUTPUT

```
