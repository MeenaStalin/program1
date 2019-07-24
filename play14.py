aim=input()
list1=["a","e","i","o","u","A","E","I","O","U"]
for inn in aim:
    if inn  in list1:
        aim=aim.replace(inn,"")
print(aim[::-1])
