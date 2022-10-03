n=input()
a="asdfghjklpoiuyqwertzxcvbnm"
arr=[]
count=0
c=""
for i in n:
    if i in a:
        arr.append(i)
    else:
        c+=i
        count+=1
i=0
arr=arr[::-1]
while count:

    ind=n.index(c[i])
    arr.insert(ind,c[i])
    i+=1
    count-=1
print("".join(arr))
        