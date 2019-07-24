branch=input()
starts=0
ends=0
for i in branch:
    if(i=="("):
        starts=starts+1
    elif(i==")"):
        ends=ends+1
if(starts==ends):
    print("yes")
else:
    print("no")
