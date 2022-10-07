n=int(input())
a=[0,1]
n=n-2
for i in range(n):
    r=a[-1]+a[-2]
    a.append(r)
print(*a)