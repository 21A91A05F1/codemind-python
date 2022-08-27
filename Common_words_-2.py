s=input().lower().split()
p=input().lower().split()
c=0
for i in s:
    if i in p:
        if (s.count(i)==1 and p.count(i)==1):
            c+=1
print(c)