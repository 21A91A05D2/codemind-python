n=int(input())
a=list(map(int,input().split()))
l=int(input())
s=0
for i in a:
    if i==l:
        s+=i
        break
    else:
        s+=i
print(s)