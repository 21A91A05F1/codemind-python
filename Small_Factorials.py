t=int(input())


while(t>0):
    n=int(input())
    i=1
    if(n==1):
        print("1")
    else:
        res=1
        while(i<=n):
            res=res*i
            i=i+1
        print(res)
    
    t=t-1