l=list(map(int,input().split(',')))
k=[]
for i in l:
    s=0
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            s+=j
    for x in l:
        if(x==s):
            c+=1
            break
    if(c):
        k.append(i)
k=sorted(k)
if(len(k)):
    print(*k)
else:
    print("-1")