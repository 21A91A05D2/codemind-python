n=int(input())

a=bin(n)
ind=a.index("b")
a=a[ind+1::]
l=[]
for i in range(len(a)):
    if a[i]=="1":
        l.append("0")
    elif a[i]=="0":
        l.append("1")

l="".join(map(str,l))
print(int(l,2))