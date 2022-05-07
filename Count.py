n=int(input())
arr=list(map(int,input().split()))
ec=0
oc=0
for i in range(n):
    if(arr[i]%2==0):
        ec=ec+1
    else:
        oc=oc+1
print(ec,oc)
        