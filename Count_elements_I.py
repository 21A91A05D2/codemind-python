n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
i=[]
l=list(a.intersection(b))
print(len(l))