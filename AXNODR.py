t=int(input())
while(t):
    n=int(input())
    if(n%4==0):
        print(n+3)
    elif(n%4==1):
        print(n)
    elif(n%4==2 or n%4==3):
        print(3)
    t-=1 