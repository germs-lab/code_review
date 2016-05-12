## this script takes the primer balst table (test.txt) and evaluates the 
## resulting fragment sizes (300-600 b), then returns the target
## genes and their corresponding primer sets. 
##
## sample input:
#```
#"genome"        "primer"        "start" "end"   "diff"
#"usdamock2_79"  "darte_qm_304_f"        373     383     NA
#"usdamock2_79"  "darte_qm_146_f"        750     762     379
#"usdamock2_79"  "darte_qm_270_r"        972     982     220
#```
## output:
#```
#genome	(primer pairs)	diff
#```

import sys

if len(sys.argv) != 2:
	sys.exit("USAGE: %s <path/to/test.txt>" % sys.argv[0])

# create a dictionary with genome as the key
# storing primer, position, and fragments as values
d = {}
for n, line in enumerate(open(sys.argv[1], 'rU')):
    info=line.rstrip().split('\t')
    if n == 0:
        continue
    else:
	genome = info[0]
	primer = info[1]
        diff = info[-1]
	# use genome as keys
	if genome not in d:
		d[genome] = [[primer], [diff]]
	else: 
		# append additional values to existing key
		d[genome][0].append(primer)
		d[genome][1].append(diff)

# create a new dictionary to manipulate values for each key
d2 = {}
for key in d:
	# create tuples for each primer pair
	primer_set=zip(d[key][0], d[key][0][1:])
	# add grouped primer sets and corresponding fragment size
	# to new dictionary d2
	d2[key] = zip(primer_set, d[key][1][1:])

for item in d2:
	# index d
	for i in range(0, len(d2[item])):
		if 300 < int(d2[item][i][1]) < 600:
			print '%s\t%s\t%s' % (item, d2[item][i][0], d2[item][i][1])	
