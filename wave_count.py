n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)-1,2):
    if(l[i-1]<l[i]):
        c+=1
    else:
        print("-1")
        c=0
        break
if(c):
    print(c)