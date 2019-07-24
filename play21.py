xs,ys=map(int,input().split())
xd,yd=map(int,input().split())
xf,yf=map(int,input().split())
a = xs * (yd - yf) + xd * (yf - ys) + xf * (ys - yd) 
if(a==0):
    print("yes")
else:
    print("no")
