n=int(input())
while n:
    
    a,b,c,d=input().split()
    n-=1
    quotient=int(a)//int(b)#2
    rem=int(a)%int(b)#0
    i=0
    j=0
    s=int(a)*int(c)#2
    for i in range(quotient):
    
        s+=int(b)*int(d)*int(j)
        i+=1
        j+=1

    p=rem*quotient*int(d)
    print(s+p)