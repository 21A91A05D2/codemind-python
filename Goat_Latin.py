s=input()
s=s.split(" ")
z=""
for i in range(len(s)):
    r=s[i]
    if r[0] in "aeiouAEIOU":
        r=r+"maa"+"a"*i
        print(r,end=" ")
    elif r=="Goat":
        print("oatGmaa",end="")
        print("a"*i,end=" ")
    else:
        p=r[0]
        r=r[1::]
        z="maa"+"a"*i
        print(r,end="")
        print(p,end="")
        print(z,end=" ")
    