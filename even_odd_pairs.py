n=int(input())
k=list(map(int,input().split()))
l=[]
m=[]
s=[]
for i in k:
    if(i%2==0):
        l.append(i)
    else:
        m.append(i)
i=0
j=0
while(i<len(l) or j<len(m)):
    if(i<len(l)):
        print(l[i],end=" ")
        i+=1
    if(j<len(m)):
        print(m[j],end=" ")
        j+=1
if(n%2):print("0")
