k=input().lower()
p=input().lower()
l=[]
c=0
for i in range(len(p)):
    i=p[i]
    if i in k and i not in l and i!=" ":
        c+=1
        l.append(i)
print(c)