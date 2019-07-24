num123,quest=map(str,input().split(" "))
counts=0
for i in num123:
    if(i==quest):
        counts=counts+1
print(counts)
