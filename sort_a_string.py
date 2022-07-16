n=input()
a=[]
b=[]
for i in n:
    if i.isalpha():
        a.append(i)
    else:
        b.append(i)
a=sorted(a)
j=0
l=len(a)
for i in range(len(n)):
    if n[i].isalpha():
        if j<l:
            
            print(a[j],end='')
            j=j+1
        
    else:
        print(n[i],end='')
        
        
  
        