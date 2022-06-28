n=int(input())
a=list(map(int,input().split()))
sumo=0
sume=0
for i in range(0,n):
    if i%2==0:
        sume+=a[i]
    else:
        sumo+=a[i]
print(abs(sume-sumo))