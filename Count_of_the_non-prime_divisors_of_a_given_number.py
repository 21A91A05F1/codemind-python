n=int(input())
def is_prime(n):
    c=0
    j=1
    while j<=n:
        if(n%j==0):
            c=c+1
        j=j+1
    if c==2:
        return 1
    else:
        return 0
i=1
d=0
while(i<=n):
    if(n%i==0):
        if(is_prime(i)==0):
            d=d+1
    i=i+1
print(d)