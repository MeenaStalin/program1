#print the shifting of the numbers
num123,keyshift=input().split()
keyshift=int(keyshift)

for i in range(keyshift):
    num123=num123[-1]+num123[:-1]
print(num123,end=' ')
