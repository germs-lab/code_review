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
        ids = '_'.join([ids,moreid[i]])
    if(annot.has_key(ids[1:])):
        temp = annot[ids[1:]]
        temp = ';'.join([temp,spl[12]])
        annot[ids[1:]] = temp
    else:
        annot[ids[1:]] = spl[12]
anread.close()
