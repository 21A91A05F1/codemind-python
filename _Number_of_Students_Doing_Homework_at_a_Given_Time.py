n=int(input())
k=list(map(int,input().split()))
m=int(input())
p=list(map(int,input().split()))
o=int(input())
c=0
for i in range(n):
    if k[i]<=o and p[i]>=o:
        c+=1
print(c)