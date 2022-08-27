l=list(map(str,input().lower().split()))
c=0
for i in range(len(l)):
    if l[i]==l[i][::-1]:
        c+=1
print(c)