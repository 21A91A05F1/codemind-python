l=list(map(str,input().split()))
a=[]
for i in range(len(l)):
    a.append(len(l[i]))
print(max(a))