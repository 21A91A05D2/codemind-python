t=int(input())
a=[]
while t:
    s=input()
    a.append(s)
    t-=1
r=a[-1]
r=r.split(" ")
print(r[-1])
