app,bpp=input().split()
app=int(app)
bpp=int(bpp)
for i in range(1,10000):
    if(i%app==0 and i%bpp==0):
        print(i)
        break
