s=input()
c=0
for i in range(len(s)):
    c=s.count(s[i])
    if c==1:
        print(i)
        break
else:
    print("-1")