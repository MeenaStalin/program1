num123,key=map(int,input().split(" "))
a123=list(map(int,input().split()))
for i in a123:
    if(i==key):
        print("Yes")
        break
else:
    print("No")
