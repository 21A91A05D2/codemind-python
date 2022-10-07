def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
i=prime(n)
s=0
while n:
    s=s*10+n%10
    n=n//10
j=prime(s)
if i==j and i==True:
    print("circular prime")
elif i==True and j==False:
    print("prime but not a circular prime")
else:
    print("not prime")