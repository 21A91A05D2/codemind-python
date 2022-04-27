a=int(input())
c=0
for i in range(2,a):
    if(i*i==a):
        c=c+1
        break
if(c==1):
    print("True")
else:
    print("False")