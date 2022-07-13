
a,b=map(int,input().split())
mat=[]
for i in range(a):
    x=list(map(int,input().split()))
    mat.append(x)
cnt=0
for j in range(b):
    z=[]
    cnt=0
    for i in range(a):
        z.append(mat[i][j])
        
    
        cnt+=mat[i][j]
    print(cnt,end=' ')