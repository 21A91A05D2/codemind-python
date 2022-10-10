t=int(input())
while t:
    s=input()
    for i in s:
        if i in "1234567890":
            print("Yes")
            break
    else:
        print("No")
    t-=1