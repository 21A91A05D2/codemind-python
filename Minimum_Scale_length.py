n=int(input())
a=list(map(int,input().split()))
c=0
res=0
for i in range(1,max(a)):
    c=0
    for j in range(0,n):
        if a[j]%i==0:
            c+=1
    if c==len(a):
        res=i
print(res)