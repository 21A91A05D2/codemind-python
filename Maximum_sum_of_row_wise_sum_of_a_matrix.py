
a,b=map(int,input().split())
mat=[]
l=[]
for i in range(a):
    x=list(map(int,input().split()))
    mat.append(x)
cnt=0
for i in range(a):
    z=[]
    cnt=0
    for j in range(b):
        z.append(mat[i][j])
        
    
        cnt+=mat[i][j]
    l.append(cnt)
print(max(l))