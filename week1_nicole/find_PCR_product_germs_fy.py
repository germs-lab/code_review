# this script recreates the last column in test file (ie "diff")
# for hits found in the same gene, it subtracts the nth row end position 
# by (n-1)th row end position to create the fragment length.
#
# note: all primer hits have to be already sorted by its hit positions for this code to work. 

import sys

if len(sys.argv) != 2:
	sys.exit("USAGE: %s <path/to/test.txt>" % sys.argv[0])

## initiating a dictionary
## to store information
## related to each genome
d = {}
for n, line in enumerate(open(sys.argv[1], 'rU')):
    info=line.rstrip().split('\t')
    ## skip the header
    if n == 0:
        continue
    else:
        genome = info[0]
	end_pos = info[-2]
	## add end position information to each unique genome
	if genome not in d:
		d[genome] = [end_pos]
	else:
		d[genome].append(end_pos)

## pull information for each genome stored
for key in d:
	## initiate a list for column "diff" with "NA" as first item
	diff_col = ["NA"]
	## create a list with multiple tuples, which contains the (n-1)th end position and the nth end position
	l = zip(d[key], d[key][1:])
	## subtract each tuples, and append results to list "diff_col"
	for x, y in l:
		diff = int(y) - int(x) 
		diff_col.append(diff)
	## create another list with tuples, where each end position and size difference are grouped together
	new = zip(d[key], diff_col)
	## print tab delimited "genome", "end position", and "diff" into different lines one line at a time
	for i in range(0, len(new)):
		print '%s\t%s\t%s' % (key, new[i][0], new[i][1]) 
	

