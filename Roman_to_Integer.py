s=input()
mapp={"I":1,"V":5,"X":10,"C":100,"L":50,"D":500,"M":1000}
n=len(s)
i=len(s)-1
out=0
while i>=0:
    if i<n-1 and mapp[s[i]]<mapp[s[i+1]]:
        out-=mapp[s[i]]
    else:
        out+=mapp[s[i]]
    i-=1
print(out)