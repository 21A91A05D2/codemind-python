n=int(input())
a=list(map(int,input().split()))
c=0
v=0
for i in range(0,len(a)-2,2):
    if a[i]<a[i+1] and a[i+1]>a[i+2]:
        c+=1
    elif a[i]>a[i+1] and a[i+1]<a[i+2]:
        c+=1
    else:
        v=-1
   
if v==-1:
    print('no')
else:
    print('yes')