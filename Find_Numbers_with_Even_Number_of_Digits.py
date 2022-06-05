n=int(input())
k=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    t=k[i]
    c=0
    while(t!=0):
        d=t%10
        c+=1
        t=t//10
    if(c%2==0):
        s+=1
print(s)
        
    