n=int(input())
temp=n
c=0
s=n*n
while(n):
    d=n%10
    c=c+1
    n=n//10
p=10**c
if(s%p==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")