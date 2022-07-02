n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if(i not in b and i not in c):
        print(i,end=' ')
for j in b:
    if(j not in a and j not in d):
        print(j,end=' ')