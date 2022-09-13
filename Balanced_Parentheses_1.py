s=input()
d={')':'(',']':'[','}':'{'}
stk=[-1]
k=0
for i in s:
    if i in("(","[","{"):
        stk.append(i)
    else:
        if (stk[-1]==d[i]):
            
           
            stk.pop()
        else:
            print("False")
            k=8
            break
if k!=8:
    print("True")
    
        