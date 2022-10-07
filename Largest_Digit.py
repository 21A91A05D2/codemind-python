n=int(input())
a=[]
while n:
    a.append(n%10)
    n=n//10
print(max(a))