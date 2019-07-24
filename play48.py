numb12=int(input())
list12=[]
for i in range(1,numb12+1):
    if(numb12%i==0):
        list12.append(i)
for num in list12:
    if(num%2!=0):
        print(num,end=" ")
