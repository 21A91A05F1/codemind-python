n=int(input())
l=list(map(int,input().split()))
k=int(input())
k=k%n
if(k==0):
    print(*l)
else:
    print(*l[-k:]+l[:n-k])