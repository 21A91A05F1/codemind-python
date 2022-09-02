t=int(input())
while(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p=[]
    for i in range(n):
        p.append(l[(n-k+i)%n])
    print(*p)
    t-=1       