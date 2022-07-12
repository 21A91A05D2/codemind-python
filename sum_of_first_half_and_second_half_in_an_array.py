n=int(input())
a=list(map(int,input().split()))
s=0
c=0
i=0
while i<n//2:
    s+=a[i]
   
    i+=1
for i in range(n//2,len(a)):
    c+=a[i]
    
    
print(s)
print(c)