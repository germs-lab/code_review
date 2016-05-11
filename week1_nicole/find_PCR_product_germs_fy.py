#writing a program to find 500 bp fragments in blast file

#Adina created the blast file and put them in order
#in R I added a column that gave the difference between two adjacent rows

#need to find the ~500 bp fragments
#and output both that row and the one before it to get both primers

#originally run on hmp_with_diff file; then mock_imperfect file

#finally on usda mock file but changed to 400-600 (from 300-700)-still hundreds

import sys

d = {}
for n, line in enumerate(open(sys.argv[1], 'rU')):
    info=line.rstrip().split('\t')
    if n == 0:
        continue
    else:
	genome = info[0]
	primer = info[1]
        diff = info[-1]
	if genome not in d:
		d[genome] = [[primer], [diff]]
	else: 
		d[genome][0].append(primer)
		d[genome][1].append(diff)

for key in d:
	primer_set=zip(d[key][0], d[key][0][1:])
	print primer_set

#        if diff != "NA" and 300 < int(diff) < 600:
#            	print n-1, 
#		print n, info, diff 
#
