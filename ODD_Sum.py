n=int(input())
a=list(map(int,input().split()))

sume=0
for i in a:
    if i%2!=0:
        sume+=i

print(sume)