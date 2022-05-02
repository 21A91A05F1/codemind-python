t=int(input())

while(t>0):
    a,b=map(int,input().split())
    i=a
    c=0
    while(i<=b):
        if(i%10==2 or i%10==3 or i%10==9):
            c=c+1
        i=i+1
    print(c)
    t=t-1