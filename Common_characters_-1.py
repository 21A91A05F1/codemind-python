s=input().lower()
l=s.split()
k=[]
w=list(l[0])
l.remove(l[0])
f=1
for i in w:
    for j in l:
        if i not in j:
            f=0
            break
    else:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    print(''.join(k))