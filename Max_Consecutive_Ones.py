n=int(input())
k=list(map(int,input().split()))
c=0
s=[]
for i in range(n):#6
    if(k[i]==1):
        c=c+1
    else:
        s.append(c)
        c=0

s.append(c)  
print(max(s))
    