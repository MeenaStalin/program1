num123=int(input())
for powers in range(100):
    if(num123==2**powers):
        print("yes")
        break
else:
    print("no")
