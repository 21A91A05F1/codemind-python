s=list(map(str,input().split()))
s="".join(s)
k=min(s)
p=max(s)
c=0
d=0
for i in range(len(s)):
    if s[i]==k:
        c=c+1
    if s[i]==p:
        d=d+1
print(k,c,p,d)