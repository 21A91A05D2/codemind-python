n=int(input())
a=list(map(int,input().split()))
a2=sorted(a)
c=0
for i in range(len(a)):
    if a[i]!=a2[i]:
        ind=a.index(a2[i])
        a[i],a[ind]=a[ind],a[i]
       
        c+=1
print(c)