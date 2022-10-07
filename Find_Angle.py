import math
a=int(input())
b=int(input())
h=math.sqrt(a*a+b*b)
h=h/2
a=a/2
angle=round(math.degrees(math.acos(a/h)))
print(angle)