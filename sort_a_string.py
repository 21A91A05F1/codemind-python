s=input()
p=""
for i in s:
    if i.isalpha():
        p+=i
p=sorted(p)
l=0
for i in s:
    if i.isalpha():
        print(p[l],end="")
        l+=1
    else:
        print(i,end="")