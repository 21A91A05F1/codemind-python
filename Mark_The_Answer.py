n,p=map(int,input().split())
k=list(map(int,input().split()))
c,d=0,0
#print(p)
#print(k)
for i in k:
    if i<=p and d<=1:
        c+=1
    else:
        d+=1
print(c)
    