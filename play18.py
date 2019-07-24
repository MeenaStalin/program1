num123=int(input())
lap=[]
for i in range(2,num123+1):
    if(num123%i==0):
        lap.append(i)
    else:
        continue
    num123=num123//i
app=sorted(lap)
print(*app)
