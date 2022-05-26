'''def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        else:
            return True
n=int(input())
sum=0
if prime(n):
    r=0
    while n:
        r=n%10
        sum=sum*10+r
        n=n//10
    if prime(sum):
        print('Twisted prime')
    else:
        print('not the twisted prime')
else:
    print('not a prime')
    twisted prime'''

    
