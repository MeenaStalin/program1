ap,bp=map(str,input(' ').split(' '))
cp=0
if len(ap)>len(bp):
    ap,bp=bp,ap
dp=0
while dp<len(ap):
      cp+=(ord(bp[dp])-ord(ap[dp]))
      dp+=1
for dp in range(dp,len(bp)):
      cp+=ord(bp[dp])-ord('a')+1
print(cp)
