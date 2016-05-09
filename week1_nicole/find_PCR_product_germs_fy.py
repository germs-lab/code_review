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
	end_pos = info[-2]
	if genome not in d:
		d[genome] = [end_pos]
	else:
		d[genome].append(end_pos)


for key in d:
	l = zip(d[key], d[key][1:])
	print [int(y) - int(x) for x,y in l]

#output=open("/Users/nicolericker/Documents/DARTE-QM/usda_500", "w")

