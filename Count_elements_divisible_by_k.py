n,se=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%se==0:
        c+=1
print(c)