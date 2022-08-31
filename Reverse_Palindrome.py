def rev(a):
    b=str(a)[::-1]
    return b

a=int(input())
while a:
    a=a+int(rev(a))
    if a==int(rev(a)):
        print(a)
        break
