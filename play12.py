num123,key_shift=map(int,input().split())
host=list(map(int,input().split()))
for inn in range(0,key_shift):
    host=[host[-1]]+host[:-1]
print(*host,end=' ')
