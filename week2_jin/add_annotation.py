#!/usr/bin/python
# this script add annotation into your abundant file
#usage: python add_annotation.py annotation abundant > output

import sys

annot = {}
anread = open(sys.argv[1],'r')
for n,line in enumerate(anread):
    if n == 0:
        continue
    spl = line.strip().split('\t')
    moreid = spl[0].split("|")[1].split("_")

    ids = ""
    for i in range(0,len(moreid)-3):
        ids = ids + "_" + moreid[i]
    if(annot.has_key(ids[1:])):
        temp = annot[ids[1:]]
        temp = temp + ";" + spl[12]
        annot[ids[1:]] = temp
    else:
        annot[ids[1:]] = spl[12]
    

fread = open(sys.argv[2],'r')
for n,line in enumerate(fread):
    spl = line.strip().split('\t')
    if n == 0:
        result = [spl[0],"description"]
        for i in range(1,len(spl)):
            result.append(spl[i])
        print '\t'.join(result)
        continue
    if (annot.has_key(spl[0])):
        des = annot[spl[0]]
    else:
        des = "unknown"
    result = [spl[0],des]
    for i in range(1,len(spl)):
        result.append(spl[i])
    print '\t'.join(result)
