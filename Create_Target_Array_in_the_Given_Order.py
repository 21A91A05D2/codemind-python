n=int(input())
a=list(map(int,input().split()))
i=int(input())
indi=list(map(int,input().split()))
arr=[]
for i in range(n):
    arr.insert(indi[i],a[i])
print(*arr)
