n=int(input())
k=list(map(int,input().split()))
for i in range(0,n,2):
    for j in range(0,k[i]):
        print(k[i+1],end=' ')
