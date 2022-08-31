n,k,q=map(int,input().split())
l=list(map(int,input().split()))
s=l[-k:]+l[:-k]
while(q):
    print(s[int(input())])
    q-=1 