ask=input()
arrays=list(map(int,input().split()))
say=1
for i in arrays:
    if arrays.count(i)==say:
        print(i)
        break;
    else:
        continue;
