s=input()
c=0
maxi=-1
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if s[j] in "aeiou":
            c+=1
            maxi=max(maxi,c)
        else:
            break
print(maxi)
        
        
    
