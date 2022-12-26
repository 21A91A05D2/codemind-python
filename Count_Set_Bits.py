t=int(input())
for i in range(t):
    n=int(input())
    s=[]
    while n!=0:
        r=n%10
        a=r%2
        s.append(a)
        n=n//2
    print(s.count(1))