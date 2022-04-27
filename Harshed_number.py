a=int(input())
s=0
n=a
while n>0:
    r=n%10
    s+=r
    n=n//10
if(a%s==0):
    print('True')
else:
    print("False")