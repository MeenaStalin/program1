str123=input()
for pork in str123:
    if(pork.islower()):
        print(pork.upper(),end="")
    else:
        print(pork.lower(),end="")
