t=int(input())
while(t):
    n=int(input())
    k=list(map(int,input().split()))
    c=0
    for i in range(len(k)):
        for j in range(len(k)):
            if(i!=j and (k[i]+k[j]) in k):
                c+=1
    if(c==0):
        print("-1")
    else:
        print(c//2)
    t-=1 