#writing a program to find 500 bp fragments in blast file

#Adina created the blast file and put them in order

#need to find the ~500 bp fragments
#and output both that row and the one before it to get both primers

#modified for code_review to calculate difference within python program
import sys

prev = []

output=open("/Users/nicolericker/Documents/Python/test_500", "w")

for n, line in enumerate(open("test.txt")):
    info=line.rstrip().split('\t')
    if n == 0:
        continue     
    else:
        check_diff = info[-1]
        if check_diff == "NA":
            num_keep = info[-2]
            prev=info
            continue
        else:
            diff=(int(info[-2])-int(num_keep))
            if 300<diff<600:
                print n, prev, info, diff
                output.write(str(prev)+str(info)+ str(diff)+"\n")
            num_keep = info[-2]
            prev = info

output.close()        



    
