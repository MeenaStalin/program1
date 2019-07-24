ans1,ans2,ans3=map(int,input().split(" "))
if(ans1!=0 and ans2!=0 and ans3!=0):
    a=ans1+ans2+ans3
else:
    a=0
if(a==180):
    print("yes")
else:
    print("no")
