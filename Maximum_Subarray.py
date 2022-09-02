n=int(input())
k=list(map(int,input().split()))
s=0
m=k[0]
for i in range(n):
    s=0
    for j in range(i,n):
        s+=k[j]
        if(m<s):
            m=s
print(m)