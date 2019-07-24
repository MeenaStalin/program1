az,bz=input().split()
az=int(az)
bz=int(bz)
cz=0
for i in range(2,bz+1):
    if(az%i==0 and bz%i==0):
         cz=i
print(cz)
