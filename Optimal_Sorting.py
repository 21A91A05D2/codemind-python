t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if b==a:
        print("0")
        break
    else:
        print(max(a)-min(a))