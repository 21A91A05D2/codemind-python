n=int(input())
a=[0,1]
n=n-2
while n:
    r=a[-1]+a[-2]
    a.append(r)
    n-=1
print(*a)