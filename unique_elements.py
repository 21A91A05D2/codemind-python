n=int(input())
a=list(map(int,input().split()))
arr=[]
for i in a:
    if i not in arr:
        arr.append(i)
print(*arr)