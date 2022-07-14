def fun(l):
   # print(l)
    l=list(l)
    c=0
    v='aeiouAEIOU'
    for i in range(len(l)):
        if l[0] in v:
            c=1
           # print(c,l[0])
            i=len(l)-1
            break
    
    if l[i] not in v:
        c=c+1
        #print(c,l[i])
    if c==2:
      #  print('k')
        return 1
    else:
        return 0
            
        

k=0
n=input().split()
for i in range(len(n)):
    k=k+fun(n[i])
print(k)
    
        
   