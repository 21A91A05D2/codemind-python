def fun(a):
    c=0
    l=[]
    for i in a:
        s=0
        temp=i
        while i:
            r=i%10
            s=s*10+r
            i=i//10
        l.append(s)
    return l
n=int(input())
a=list(map(int,input().split()))
print(*fun(a))