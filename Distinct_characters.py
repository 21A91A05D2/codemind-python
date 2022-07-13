n=input()
n=n.lower()
a=[]
for i in n:
    c=n.count(i)
    if c==1 and (ord(i)<65 or ord(i)>90):
        a+=i
    c=0
if(a.count(" ")>=1):
    j=a.index(" ")
    a.pop(j)
a.sort()
a="".join(a)
print(a)