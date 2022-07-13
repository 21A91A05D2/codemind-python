n=input()
n=n.lower()
a=[]
k=8
for i in n:
    c=n.count(i)
    if c==1:
        print(i)
        k=0
        break
    c=0
if k!=0:
    print('-1')
