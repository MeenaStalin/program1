asa,bsa=map(str,input().split())
counts=0
for inn in range(len(asa)):
    #for jnn in range(0,len(bsa)):
    if(asa[inn]!=bsa[inn]):
        counts=counts+1
if(counts==1):
    print("yes")
else:
    print("no")
