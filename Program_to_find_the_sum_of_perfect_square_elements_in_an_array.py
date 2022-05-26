def is_square(m):
    p=int(m**0.5)
    if(p*p==m):
        return 1
    else:
        return 0
n=int(input())
k=list(map(int,input().split()))
s=0
for i in range(len(k)):
    if(is_square(k[i])):
        s=s+k[i]
print(s)
      