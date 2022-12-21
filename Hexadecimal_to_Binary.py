n=int(input())
while(n):
    h=input()
    n-=1
    k=int(h,16)
    m=bin(k)
    m=m.replace("0b","")
    l=len(m)
    if l%4==0:
        print(m)
    else:
        l=l%4
        j=""
        for i in range(4-l):
            j+=str(0)
        j+=m
        print(j)
    