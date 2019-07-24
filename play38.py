num123=int(input())
list123=[]
for i in range(2,num123+1):
    if(num123%i==0):
        list123.append(i)
for numb in list123:
    if(numb%2==0):
        print(numb,end=" ")
