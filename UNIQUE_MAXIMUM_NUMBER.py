n=int(input())
a=list(map(int,input().split()))
c=0
v=0
b=[]
for i in range (0,n):
    c=0
    for j in range(0,n):
        if a[i]!=a[j]:
            c+=1
            if c==n-1:
                b.append(a[i])
                v+=1
if v==0:
    print('-1')
else:
    print(max(b)) 
