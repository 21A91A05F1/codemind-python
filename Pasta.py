n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in b:
    if i in a:
        a.remove(i)
    else:
        c+=1
        break
if(c==0):
    print("Yes")
else:
    print("No")