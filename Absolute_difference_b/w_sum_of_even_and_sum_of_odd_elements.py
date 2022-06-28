n=int(input())
a=list(map(int,input().split()))
sumo=0
sume=0
for i in a:
    if i%2==0:
        sume+=i
    else:
        sumo+=i
print(abs(sume-sumo))