t=int(input())
while t:
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        r=i%10
        if r==3 or r==2 or r==9:
            c+=1
    t-=1
    print(c)