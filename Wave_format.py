n=int(input())
k=list(map(int,input().split()))
k=sorted(k)[::-1]
l=[]
for i in range(n):
    if(i%2==1):
        l.append(k[i])
        l.append(k[i-1])
if(n%2==1):
    l.append(k[n-1])
print(*l)