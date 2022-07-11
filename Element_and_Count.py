n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in a:
    p=0
    if i not in l:
        p=a.count(i)
        l.append(i)
        print(i,p,end=' ')
