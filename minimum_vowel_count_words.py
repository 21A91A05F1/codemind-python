k=list(map(str,input().split()))
p="aeiouAEIOU"
c=0
b=[]
for i in k:
    s=i
    c=0
    for j in range(len(s)):
        if s[j] in p:
            c=c+1
    b.append(c)
v=min(b)
x=0
for i in b:
    if i==v:
        x=x+1
print(x)

    