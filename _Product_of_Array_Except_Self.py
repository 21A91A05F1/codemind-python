n=int(input())
m=list(map(int,input().split()))
p=1
s=[]
for i in range(len(m)):
    p=p*m[i]
for i in range(len(m)):
    s.append(p//m[i])
print (*s)
   