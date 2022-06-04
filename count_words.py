l=list(map(str,input().split()))
k='aeiouAEIOU'
c=0
for i in range(len(l)):
    for j in range(len(l[i])):
        t=l[i]
        if t[0] in k and t[len(l[i])-1] not in k:
            c+=1
            break
print(c)