s=input()
k="aeiouAEIOU"
c=0
l=[]
for i in s:
    c=1
    if i in k:
        if i not in l:
            l.append(i)
print(*l)
if(c==0):
    print(-1)
