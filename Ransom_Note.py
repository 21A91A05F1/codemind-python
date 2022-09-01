a,b=map(str,input().split())
b=list(b)
c=0
for i in a:
    if i in b:
        c+=1
        b.remove(i)
if(c==len(a)):
    print("True")
else:
    print("False")