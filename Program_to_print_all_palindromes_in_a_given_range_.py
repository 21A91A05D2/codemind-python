def fun(n):
    su=0
    while n:
        r=n%10
        su=su*10+r
        n=n//10
    return su
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i==fun(i):
        print(i,end=" ")