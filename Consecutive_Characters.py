n=input()

c=1
count=0
for j in range(0,len(n)-1):
    if n[j]==n[j+1]:
        c+=1
    else:
        if count<c:
            count=c
        c = 1

if count<c:
    count=c
print(count)