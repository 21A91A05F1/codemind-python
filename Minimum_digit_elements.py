n=int(input())
a=list(map(int,input().split()))
p=[]
for i in range(len(a)):
    a[i]=str(a[i])
    p.append(len(a[i]))
print(p.count(min(p)))
    
