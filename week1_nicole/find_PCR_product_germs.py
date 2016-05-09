#writing a program to find 500 bp fragments in blast file

#Adina created the blast file and put them in order
#in R I added a column that gave the difference between two adjacent rows

#need to find the ~500 bp fragments
#and output both that row and the one before it to get both primers

#originally run on hmp_with_diff file; then mock_imperfect file

#finally on usda mock file but changed to 400-600 (from 300-700)-still hundreds

import sys

for n, line in enumerate(open("test.txt")):
    info=line.rstrip().split('\t')
    if n == 0:
        continue
    else:
        num_keep = info[-2]
        check_diff = info[-1]

        if check_diff == "NA":
            print n, info, num_keep
            continue
        num_keep = info[-2]
        print n, info, num_keep

#output=open("/Users/nicolericker/Documents/DARTE-QM/usda_500", "w")

#prev = []


#with open("/Users/nicolericker/Documents/DARTE-QM/usda_with_diff") as data:
#    start=False
#    for line in data:
#    if "diff" in line:
#        continue
#    print line,
#            break
#    for line in data:
#        if "NA" in line:
#            break
#    for line in data:
#        info=line.rstrip().split('\t')
#        difference = int(data[-1])
        #print(difference)
#        if (400<difference<600):
#            output.write(str(prev)+str(info)+ "\n")
#        prev=data

#output.close()

#print("Finished!")

    
