a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
p=[]
for i in l:
    if i not in m and i not in p:
        p.append(i)
for i in m:
    if i not in l and i not in p:
        p.append(i)
print(*p)