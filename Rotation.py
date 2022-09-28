t=int(input())
while t:
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
   
    a[:]=a[n-b:]+a[:n-b]
    print(*a)
    t-=1