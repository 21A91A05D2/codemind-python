n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in range(max(len(e),len(o))):
    if i<len(e):
        print(e[i],end=" ")

    if i<len(o):
        print(o[i],end=" ")
  
if n%2!=0:
    print("0")