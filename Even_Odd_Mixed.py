n=int(input())
c1=0
c2=0
c=0
while n!=0:
    rem=n%10
    c=c+1
    if rem%2==0:
        c1=c1+1
    else:
        c2=c2+1
    n=n//10
if c1==c:
    print("Even")
elif c2==c:
    print("Odd")
else:
    print("Mixed")