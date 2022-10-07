n=int(input())
for i in range(1,n+1):
    if 2**i<=n:
        a=2**i
    else:
        b=2**i
        break
if abs(a-n)<=abs(b-n):
    print(abs(a-n))
else:
    print(abs(b-n))