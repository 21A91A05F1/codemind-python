n=int(input())
rev=0
c1=0
c2=0
temp=n
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
n=temp;
i=2
while(i<n):
    if(n%i==0):
        c1=c1+1
    
    i=i+1
i=2
while(i<rev):
    if(rev%i==0):
        c2=c2+1
    i=i+1

if(c1==0 and c2==0):
    print("circular prime")
elif(c1==0):
    print("prime but not a circular prime")
else:
    print("not prime")
    
