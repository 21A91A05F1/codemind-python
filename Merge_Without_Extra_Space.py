t=int(input())
while(t):
    x,y=map(int,input().split())
    k=list(map(int,input().split()))
    p=list(map(int,input().split()))
    s=sorted(k+p)
    print(*s)
    t=t-1