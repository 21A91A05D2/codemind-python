n=int(input())
a=list(map(int,input().split()))
arr=[]
for i in range(1,n,2):
    r=a[i-1]
    while r:
        arr.append(a[i])
        r-=1
print(*arr)