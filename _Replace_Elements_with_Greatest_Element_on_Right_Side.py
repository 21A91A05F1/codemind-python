n=int(input())
k=list(map(int,input().split()))
p=[]
for i in range(n-1):
    p.append(max(k[i+1:]))
p.append(-1)
print(*p)
