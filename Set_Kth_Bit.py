m,n=map(int,input().split())
s=[]
for i in range(n+1):
    if i==n:
        s.append(1)
    else:
        s.append(0)
t=0
j=0
for i in s:
    t=t+(i*(2**j))
    j+=1
print(m|t)