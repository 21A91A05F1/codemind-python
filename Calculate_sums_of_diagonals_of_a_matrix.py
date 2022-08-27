a=int(input())
s=0
s1=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in range(a):
        if(i==j):
            s+=(arr[j])
        if(i+j==a-1):
            s1+=(arr[j])
print("Principal Diagonal:",end="")
print(s)
print("Secondary Diagonal:",end="")
print(s1)