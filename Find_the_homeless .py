t=int(input())
h=[]
p=[]
k=t
r=t
while t:
    a=int(input())
    p.append(a)
    t-=1
while k:
    a=int(input())
    h.append(a)
    k-=1
c=0
for i in range(len(p)):
    l=p[i]
    for j in range(len(h)):
        if l<=h[j]:
            h[j]=-1
            c+=1
            break
print(abs(c-r))