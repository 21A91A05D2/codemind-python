def rotate(a,n,r):
    b=[]
    for i in range((n-r)%n,n):
        b.append(a[i])
    
    for i in range(0, (n-r)%n):
        b.append(a[i])
 
    return b
n=int(input())
a=list(map(int,input().split()))
r=int(input())

print(*rotate(a,n,r))
