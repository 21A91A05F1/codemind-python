n=int(input())
i=1
c=0
while(i<=n):
    if(n%i==0):
        c+=1
    i+=1
if(c==2):
    print("prime")
else:
    print("not a prime")