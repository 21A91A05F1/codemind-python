a=int(input())
b=int(input())
c=0
i=a+1
flag=0
while(i<b):
    flag=0
    j=2
    while(j<=i/2):
        if(i%j==0):
            flag=1
            break
        j=j+1
    if(flag==0):
        print(i)
    i=i+1
            