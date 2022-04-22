n=int(input())
c=0
for x in range(1000000):
    if(x*(x+1)==n):
        c+=1
if(c>0):
    print("YES")
else:
    print("NO")