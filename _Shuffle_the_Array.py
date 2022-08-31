n=int(input())
l=list(map(int,input().split()))
k=n//2
p=[]
for i in range(k):
    p.append(l[i])
    p.append(l[i+k])
print(*p)