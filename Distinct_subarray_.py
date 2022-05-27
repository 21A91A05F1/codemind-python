n=int(input())
m=int(input())
c=0
s=0
for i in range(n,m+1):
    s=0
    for j in range(i,m+1):
        s=s+j
        if(s%2!=0):
            c=c+1
print(c)