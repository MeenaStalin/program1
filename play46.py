import math
angles=int(input())
b2=math.radians(angles)
y=math.sin(b)
if(b2<1):
    print(round(y,1))
elif(b2>1):
    print(round(y))
