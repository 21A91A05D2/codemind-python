s=input()
c,p=0,0
for i in s:
    if i=="I":
        print(c,end=" ")
        c+=1
    if i=="D":
        print(len(s)-p,end=" ")
        p+=1
print(c)