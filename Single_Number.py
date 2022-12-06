from collections import Counter
n=int(input())
k=list(map(int,input().split()))
c=Counter(k)
for i,j in c.items():
    if(j==1):
        print(i)
        break