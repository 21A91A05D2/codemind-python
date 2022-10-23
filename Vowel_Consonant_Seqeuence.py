s=input()
a=""
if s[0] in "AEIOUaeiou":
    a+="V"
else:
    a+="C"
for i in range(1,len(s)):
    if s[i] in"AEEIOUaeiou":
        j="V"
    else:
        j="C"
    if a[-1]!=j:
        a+=j
print(a)
    