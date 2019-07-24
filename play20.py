str123=input()
fin=[]
ail=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in str123:
    if(i=="X"):
        fin.append("A")
    elif(i=="Y"):
        fin.append("B")
    else:
        fin.append(ail[ail.index(i)+3])
print("".join(fin))
