n=int(input())

sum=0
temp=n
while(n>0):
    d=n%10
    sum=sum+d
    n=n//10
if(temp%sum==0):
    print("True")
else:
    print("False")