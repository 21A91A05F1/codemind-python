a,b,c=map(int,input().split())
s=(a+b+c)/2

a=(s*(s-a)*(s-b)*(s-c))
import math
x=math.sqrt(a)
print ('{:.2f}'.format(x))