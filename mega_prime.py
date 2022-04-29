n=int(input())
def is_prime(n):
    c=0
    i=1
    while i<=n:
        if(n%i==0):
            c=c+1
        i=i+1
    if c==2:
        return 1
    else:
        return 0
c1=0
c2=0
if(is_prime(n)==1):
    t=n
    while(n!=0):
        d=n%10
        c1=c1+1
        if (is_prime(d)==1:
            c2=c2+1
        n=n//10
    if c1==c2:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")