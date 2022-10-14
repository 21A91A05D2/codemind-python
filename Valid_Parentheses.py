def fun(s):
    
    l=len(s)
    if l%2!=0:
        return False
        
    mapp={")":"(","]":"[","}":"{"}
    sen=[]
    for i in s:
        if i in ['(',"[","{"]:
            sen+=i
        else:
            if sen and sen[-1]==mapp[i]:
                sen.pop()
            else:
                return False
    return True if not sen else False
n=int(input())
while n:
    s=input()
    print(fun(s))
            
    n-=1