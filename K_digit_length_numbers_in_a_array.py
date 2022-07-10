n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i<0:
        i=str(-i)
    else:
        i=str(i)
    if len(i)==m:
        c+=1

print(c)