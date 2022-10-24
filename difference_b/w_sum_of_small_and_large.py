s=input()
s=s.split()
l=[]
for i in range(len(s)):
    k=s[i]
    l.append(sorted(k))
a=[]
b=[]
for i in range(len(l)):
    x=l[i]
    a.append(x[0])
    b.append(x[-1])
d,e=0,0
for i in range(len(a)):
    d+=ord(a[i])
    e+=ord(b[i])
print(abs(d-e))
    