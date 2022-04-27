a=int(input())
s=0
n=a
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if(s==a):
    print('True')
else:
    print("False")