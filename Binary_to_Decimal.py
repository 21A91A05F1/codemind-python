n=int(input())
while(n):
    k=int(input())
    r,i=0,0
    while(k):
        d=k%10
        r=r+d*pow(2,i)
        k=k//10
        i+=1
    print(r)
        
    n-=1