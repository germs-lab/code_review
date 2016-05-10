# this script recreates the last column in test file (ie "diff")
# for hits found in the same gene, it subtracts the nth row end position 
# by (n-1)th row end position to create the fragment length.
#
# note: all primer hits have to be already sorted by its hit positions for this code to work. 

import sys

d = {}
for n, line in enumerate(open(sys.argv[1], 'rU')):
    info=line.rstrip().split('\t')
    if n == 0:
        continue
    else:
        genome = info[0]
	end_pos = info[-2]
	if genome not in d:
		d[genome] = [end_pos]
	else:
		d[genome].append(end_pos)
d2 = {}
for key in d:
	diff_col = ["NA"]
	l = zip(d[key], d[key][1:])
	for x, y in l:
		diff = int(y) - int(x) 
		diff_col.append(diff)
	new = zip(d[key], diff_col)
	for i in range(0, len(new)):
		print '%s\t%s\t%s' % (key, new[i][0], new[i][1]) 
	

