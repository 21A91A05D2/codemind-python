n=int(input())
fa=fb=2
fn=0
for i in range(n):
    if i==n-1:
        print(fa)
    fn=fa+fb
    fa=fb
    fb=fn
