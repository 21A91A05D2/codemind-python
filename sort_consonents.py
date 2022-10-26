s=input().split(" ")

for i in s:
    c=[]
    for j in range(len(i)):
        if i[j] not in "AEIOUaeiou":
            c.append(i[j])
    c.sort()
    k=0
    for j in range(len(i)):
        if i[j] in "AEIOUaeiou":
            print(i[j],end="")
        else:
            print(c[k],end="")
            k+=1
    print(end=" ")