n=int(input())
a=list(map(int,input().split()))
c=0
v=0
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        c=0
    else:
        v=-1
    

if v==-1:
    print('no')
else:
    print('yes')