def fun(n):
    s=0
    t=n
    while n:
        s=s*10+n%10
        n=n//10
    if s==t:
        return 1
    return 0
n=int(input())
num=n
res1=0
temp=n-1
n=n+1
while n:
    if fun(n):
        res1=n
        break
    n+=1
res2=0
while temp:
    if fun(temp):
        res2=temp
        break
    temp-=1
if abs(res1-num)<abs(res2-num):
    print(res1)
elif abs(res1-num)>abs(res2-num):
    print(res2)
else:
    print(res2,res1)
