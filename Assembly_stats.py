import HTSeq
import random
import argparse
import numpy 

parser = argparse.ArgumentParser() #simplifys the wording of using argparse as stated in the python tutorial
parser.add_argument("-i", type=str, action='store',  dest='input', help="input the read file") # allows input of the genome
parser.add_argument("-r1", type=str, action='store', required=False,  dest='Read1', help="R1 file") # allows input of the forward read
parser.add_argument("-r2", type=str, action='store', required=False,  dest='Read2', help="R2 file") # allows input of the forward read
parser.add_argument("-o", type=str, action='store',  dest='output', help="output the read file") # allows output name
args = parser.parse_args()

INPUT = str(args.input)
OUTPUT = str(args.output)


inputfile = HTSeq.FastaReader( INPUT )

listolengths = numpy.fromiter((len(x) for x in inputfile), int)

# listolengths = []
# counter = 0

# for read in inputfile:
#       length = len(read)
#       listolengths.append(length)
#       counter +=1

print ("There are %d contigs/reads in this file" % len(listolengths))

#Sorts out the list of lengths from largest to smallest 







# Print stats about file
#N50 is the length of the read at which 50 of all bases are accounted for above it, therefore I should add up all the values in the list and then work my way from the largest to the smallest 

#N50 caluclation

# Example examplelist = [1,1,1,1,4,4,5,6,7,8,8,8,9,] which is 63 in total which halved is 31, which means N50 would be (9+8+8+8) = 33 so 7 is the next value so would be the N50.

listolengths.sort()

allnums = listolengths.sum()

print ("Total number of contigs is: %d" %len(listolengths))


print ("Total number of bases in all contigs/reads is: %d" %allnums)


halfway = allnums / 2

print ("The halfway value is: %d" % halfway)
N50counter = 0


for i in reversed(listolengths):
        if N50counter < halfway:
                N50counter += i
                #print ("%d has been added to N50" % i)
        elif N50counter >= halfway:
                N50here = i
                break
print ("N50 is: %d" % N50here)



# Print largest


print ("%d is the size of the largest contig/read" % listolengths.max() )




print ("%d is the smallest contig/read" % listolengths.min())




## Print coverage

if args.Read1 is not None:
    if args.Read2 is not None: # Double reads
        readfile = HTSeq.FastqReader(args.Read1)
        readbases1 = numpy.fromiter((len(x) for x in readfile), int)
        readfile = HTSeq.FastqReader(args.Read2)
        readbases2 = numpy.fromiter((len(x) for x in readfile), int)
        coverage = (readbases1.sum()+readbases2.sum())/float(allnums)
    else:
        readfile = HTSeq.FastqReader(args.Read1)
        readbases1 = numpy.fromiter((len(x) for x in readfile), int)
        coverage = float(readbases1.sum())/float(allnums)        

print ("Coverage is: %d" %float(coverage))

