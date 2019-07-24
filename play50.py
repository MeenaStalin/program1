numbs=int(input())
for i in range(2,numbs):
    if(numbs%i==0):
        print("yes")
        break
else:
    print("no")
