n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)-1,2):
    num=a[i+1]
    while num:
        print(a[i],end=' ')
        num-=1