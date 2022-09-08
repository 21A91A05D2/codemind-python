n=int(input())
a=input()
a=list(a)
s=0
for i in range(0,len(a)-1):
    s+=abs(int(a[i+1])-int(a[i]))

s=n-s-1
if s%3==0:
    print("Sudhir")
   
else:
    print("Ashok")
    