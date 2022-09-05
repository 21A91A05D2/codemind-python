n=int(input())
arr=list(map(int,input().split()))
k=arr[0];
c=0
v=0
for i in arr:
    if i==k:
        c+=1
if c==n:
    print("0")
else:
    for i in range(n):
        c=0
        for j in range(i,n):
            if arr[i]==arr[j]:
                
                c+=1
                if c>v:
                    v=c
    print(v)
   