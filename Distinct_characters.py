s=input().lower()
l=[]
for i in s:
    if s.count(i)==1 and i!=' ':
        l.append(i)
        l.sort()
r=''
for i in l:
    r+=i
print(r)