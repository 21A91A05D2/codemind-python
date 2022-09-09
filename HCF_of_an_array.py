a=int(input())
arr=list(map(int,input().strip().split()))
m=max(arr)
for i in range(m,-1,-1):
    c=0
    for j in range(0,a):
        if(arr[j]%i==0):
            c+=1
    if(c==a):
        hcf=i
        i=0
        break
    if i==0:
        break
print(hcf)