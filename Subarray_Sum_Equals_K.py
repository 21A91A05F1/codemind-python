n,k=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=l[j]
        if(s==k):
            p+=1
print(p)
            
