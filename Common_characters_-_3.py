s=input().lower().split()
l=[]
p=s[0]
for i in p:
    for j in s:
        if(i==" "):
            continue
        elif i in j:
            continue
        else:
            break
    else:
        l.append(i)
if(len(l)):
    print(min(l))
else:
    print(-1)

            