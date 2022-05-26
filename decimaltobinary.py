'''def dec(m):
    while m>0:
        r=m%2
        m=m//2
        for i in range(r+1,0,-1):
            print(r,end=' ')
    if n==1:
        return 1
m=int(input())
dec(m)'''
'''def dec(n):#decimal to binary
    s=''
    while n>1:
        r=n%2
        n//2
        s+=str(r)
    s+=str(n)
    return s[ : :-1]
n=int(input())
print(bin(n),end=' ')
'''
'''def binary(n):
    r=0
    i=0
    while n:#infinate loop
        rem=n%10
        r+=((2**i)*rem)
        n//=10# 101 10 1 0
        i+=1
    return r
n=int(input())
print(binary(n))#binary to decimal'''



        
