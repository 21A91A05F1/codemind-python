n=int(input())
k=list(map(int,input().split()))
p=[]
for i in range(0,n,2):
    for j in range(k[i+1]):
        p.append(k[i])
print(*p)

        
