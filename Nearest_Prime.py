def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
t=int(input())
while t:
    a=int(input())
    for i in range(a,a+100):
        if prime(i):
            res1=i
            break
    for i in range(a,0,-1):
        if prime(i):
            res2=i
            break
    if abs(a-res1)>abs(a-res2):
        print(res2)
    elif abs(a-res1)==abs(a-res2):
        print(res2)
    else:
        print(res1)
    t-=1