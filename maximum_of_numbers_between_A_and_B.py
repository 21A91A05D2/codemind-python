n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
co=0
x=[]
for i in a:
    if(i>=b and i<=c and i not in x):
        co+=1
        x+=[i]
if(co==0):
    print('-1')

else:
    print(max(x))