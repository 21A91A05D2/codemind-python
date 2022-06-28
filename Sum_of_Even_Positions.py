n=int(input())
a=list(map(int,input().split()))
sume=0
for i in range(n):
    if i%2==0:
        sume+=a[i]

print(sume)