n=int(input())
m=int(input())

s1=0;
s2=0;
i=1;
while(i<n):
    if(n%i==0):
        s1=s1+i
    i=i+1
i=1
while(i<m):
    if(m%i==0):
        s2=s2+i;
    i=i+1;
if(s1==m and s2==n):
    print("Amicable")
else:
    print("Not Amicable")
    