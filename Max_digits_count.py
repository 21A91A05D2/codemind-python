def count(i):
    c=0
    while i>0:
        r=i%10
        i=i//10
        c+=1
    return c
n=int(input())
s=[]
a=list(map(int,input().split()))

for i in a:
    s.append(count(i))
z=max(s)
print(s.count(z))