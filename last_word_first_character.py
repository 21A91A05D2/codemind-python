def fun(l):
  
    l=list(l)
    return l[0]
            
        

k=0
n=input().split()
for i in range(len(n)):
    k=fun(n[i])
print(k)
    
        
   