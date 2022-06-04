k=list(map(str,input().split()))
p="aeiouAEIOU"
b=[]
for i in k:
    s=i
    c=0
    for j in range(len(s)):
        if s[j] in p:
            c=c+1
    b.append(c)
print(min(b))
    