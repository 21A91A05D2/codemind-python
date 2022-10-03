n=input()
a=[]
array="1234567890"
for i in n:
    if i in array:
        if i not in a:
            a.append(i)
a=sorted(a)
i=0
k=9
for i in range(i,len(a)-1):
    if int(a[i])%2!=0:
        #print(a[i],a[i+1])
        a[i],a[i+1]=a[i+1],a[i]
        if int(a[i])%2==0:
            print("".join(a[::-1]))
            k=8
            break
        
    else:
        a=a[::-1]
        k=8
        print("".join(a))
        break
if k!=8:
    print("-1")