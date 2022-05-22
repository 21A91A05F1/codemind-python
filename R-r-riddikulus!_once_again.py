n,k=map(int,input().split())
l=list(map(int,input().split()))
k=k%n
k=abs(k-n)
if(k==0):
    print(*l)
else:
    print(*l[-k:]+l[:n-k])