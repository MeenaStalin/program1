a123,b123=input().split(" ")
a123=int(a123)
b123=int(b123)
count1=0
for inn in range(a123,b123+1):
    if(inn>1):
        for jnn in range(2,inn):
            if(inn%jnn==0):
                break
                
        else:
            count1=count1+1
print(count1)
