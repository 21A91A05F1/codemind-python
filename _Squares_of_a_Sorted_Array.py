n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(n):
    k.append(arr[i]*arr[i])
print(*sorted(k))
 