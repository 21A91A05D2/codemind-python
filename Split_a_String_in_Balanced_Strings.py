n=input()
r,l,c=0,0,0
for i in n:
    if i=="R":
        r+=1
    elif i=="L":
        l+=1
    if r==l:
        c+=1
        r=0
        l=0
print(c)