n=int(input())
m=int(input())
r=0
for i in range(n,m+1):
    a=i
    while(a):
         d=a%10
         r=r*10+d
         a=a//10
   
    if(r==i):
        print(i,end=' ')
    r=0