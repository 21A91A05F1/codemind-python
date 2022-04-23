a,b=map(int,input().split())
if(a>b):
    dividened=a
    divisor=b
else:
    dividened=b
    divisor=a
while(divisor):
    d=dividened%divisor
    dividened=divisor
    divisor=d
print(dividened)
    