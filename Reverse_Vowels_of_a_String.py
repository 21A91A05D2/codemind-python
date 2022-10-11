s=input()
v=[]
for i in range(len(s)):
    if s[i] in "AEIOUaeiou":
        v.append(s[i])
l=len(v)-1
for j in range(len(s)):
    if s[j] in "AEIOUaeiou":
        
        print(v[l],end="")
        l-=1
    else:
        print(s[j],end="")
