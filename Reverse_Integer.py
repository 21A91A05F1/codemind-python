n=int(input())
r=0
temp=n
if(n<0):
    n=abs(n)
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(temp>0):
    print(r)
else:
    print(-r)