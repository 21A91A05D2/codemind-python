def fun(a):
    s=[]
    for i in range(0,len(a)):
        if a[i]=='#':
            s.pop()
        else:
            s.append(a[i])
    return s
        
a=input()
b=input()
p=fun(a)
q=fun(b)

if p==q:
    print("True")
else:
    print("False")