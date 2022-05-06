n=int(input())
k=n//2+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j :
            print(0,end='')
        else:
            print( 'x',end='')
    print()