n=int(input())
l=list(map(int,input().split()))
p=0
for i in range(n):
    for j in range(i,n):
        if l[j]-l[i]>p:
            p=l[j]-l[i]
print(p)