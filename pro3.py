m1,m2=input(' ').split(' ')
sky=abs(len(m1)-len(m2))
for i in range(len(m1)):
    if len(m2)==1 and m2[i] in m1:
        break
    if m1[i] != m2[i]:
       sky+=1 
print(sky)
