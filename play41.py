num,mum=map(int,input().split())
gates=1
for i in range(1,100):
      if(pow(mum,i)==num):
        print("yes")
        gates=0
        break
if(gates==1):
    print("no")
