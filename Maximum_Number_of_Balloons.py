n=input()
b,a,l,o,p=0,0,0,0,0
for i in range(len(n)):
    if n[i]=="b":
        b+=1
    elif n[i]=="a":
        a+=1
    elif n[i]=="l":
        l+=1
    elif n[i]=="o":
        o+=1
    elif n[i]=="n":
        p+=1
print(min(b,a,l//2,o//2,p))