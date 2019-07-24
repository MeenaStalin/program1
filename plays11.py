ask=input()
if ask[-3:]=="day":
    if(ask=="Sunday" or ask=="Saturday"):
        print("yes")
    else:
        print("no")
else:
    print("invalid")
