aim=input()
list1=["a","e","i","o","u","A","E","I","O","U"]
for i in aim:
    if i in list1:
        aim=aim.replace(i,"")
print(aim[::-1])
