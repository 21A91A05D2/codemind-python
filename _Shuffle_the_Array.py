n=int(input())
a=list(map(int,input().split()))
v=[]
h=n//2
for i in range(0,h):
    v.append(a[i])
    i=i+h
    v.append(a[i])
    i=i-h
print(*v)