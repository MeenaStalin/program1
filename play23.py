as,bs=map(int,input().split(" "))
a123=list(map(int,input().split(" ")))
a234=list(map(int,input().split(" ")))
for i in a234:
    a123.insert(0,i)
    c3=max(a123)
    print(c3,end=" ")
