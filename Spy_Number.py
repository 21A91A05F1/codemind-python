n=int(input())
sum=0
p=1
while(n>0):
    d=n%10
    sum=sum+d
    p=p*d
    n=n//10
if(sum==p):
    print("Spy Number")
else:
    print("Not Spy Number")