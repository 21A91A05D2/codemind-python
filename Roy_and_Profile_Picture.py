l=int(input())
t=int(input())
while t:
    w,h=map(int,input().split())
    if w==h and w>=l and h>=l:
        print("ACCEPTED")
    elif w<l or h<l:
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")
    t-=1