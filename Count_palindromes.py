def fun(a):
    c=0
    for i in a:
        s=0
        temp=i
        while i:
            r=i%10
            s=s*10+r
            if s==temp:
                c+=1
            i=i//10
    return c
n=int(input())
a=list(map(int,input().split()))
print(fun(a))