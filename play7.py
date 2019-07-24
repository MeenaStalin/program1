tell=input()
for kin in range(len(tell)):
    if (kin%2==0):
        print(tell[kin+1],end='')
    else:
        print(tell[kin-1],end='')
