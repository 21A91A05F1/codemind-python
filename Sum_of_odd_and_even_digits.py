n=int(input())

arr=list(map(int,input().split()))
k=len(arr)
o=0
e=0
for i in range(k):
    if(i%2==0):
        e=e+arr[i]
    else:
        o=o+arr[i]
if(o-e==0):
    print("YES")
else:
    print("NO")