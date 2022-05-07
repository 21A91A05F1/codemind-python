n=int(input())
val=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+val[i]
print(s)