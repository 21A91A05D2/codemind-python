def prime(i):
    if i==1:
            return 0
    elif i==2:
        return -1
    for j in range(2,i):
        
        if i%j==0:
            return 0
    else:
        return -1
n=int(input())
a=list(map(int,input().split()))
s,c=0,0
for i in a:
    if prime(i):
       
        s+=i
        c+=1
m=s/c
print('%.2f'%m)