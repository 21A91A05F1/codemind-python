k=list(map(str,input().split()))
p=list(map(str,input().split()))

s=[]
for i in range(len(k)):
    for j in range(len(p)):
        if(k[i].lower()==p[j].lower()):
            s.append(k[i])
print(len(s))