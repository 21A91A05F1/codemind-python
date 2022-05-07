n=int(input())
m=int(input())
s=0
arr=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        s=s+arr[i][j]
print(s)