p,r,t=map(int,input().split())
a=(1+(r/100))**t
x=('{:.2f}'.format(a*p))
print (x)