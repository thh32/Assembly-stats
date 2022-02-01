# Assembly-stats
Provides some of the common assembly statistics used to identify how good a metagenomic assembly is.


##Statistics  
- N50
- Total bases in assembly
- Number of contigs
- Longest contig
- Smallest contig
-  Coverage



##Usage

Use Assembly_stats.py like so;
```
python Assembly_stats.py  -i $INPUT -r1 $READ1 -r2 $READ2 -o $OUTPUT

```

The code works with both single and paired end data.
