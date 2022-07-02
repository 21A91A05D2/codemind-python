n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
p,q=0,0
for i in a:
    if(i not in b and i not in c):
        c+=[i]
        p+=1
for j in b:
    if(j not in a and j not in d):
        d+=[j]
        q+=1
print(p+q)