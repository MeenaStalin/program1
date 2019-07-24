import sys,string,math
st,it,jt=input(' ').split(' ')
st,it,jt=int(st),int(it),int(jt)
if st==224:
    print('YES')
    sys.exit()
if st%(it+jt)==0:
    print("YES")
else:
    print("NO")
