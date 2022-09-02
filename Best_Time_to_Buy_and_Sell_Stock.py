n=int(input())
k=list(map(int,input().split()))
m=0
for i in range(n):
    for j in range(i,n):
        if(k[i]<k[j]):
            r=k[j]-k[i]
            if(m<r):
                m=r
print(m)