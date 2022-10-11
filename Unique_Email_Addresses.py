t=int(input())
d=[]
while t:
    s=input()
    st=""
    ind=s.index("@")
    for i in range(len(s)):
        if s[i]==".":
            pass
        elif s[i]=="+":
            break
        
        else:
            st+=s[i]
    
    st+=s[ind::]
    d.append(st)
    
    t-=1
d=set(d)
print(len(d))