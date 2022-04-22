n=int(input())
sum=0
res=n*n
while (res>0):
    d=res%10
    sum=sum+d
    res=res//10
if (sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")