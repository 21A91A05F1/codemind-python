a,b=map(int,input().split())
k=list(map(int,input().split()))
p=list(map(int,input().split()))
s=[]
for i in k:
    if i in p and i not in s:
        s.append(i)
print(*s)