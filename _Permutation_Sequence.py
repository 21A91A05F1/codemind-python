from itertools import permutations
n,k=map(int,input().split())
s=""
l=[]
c=0
for i in range(1,n+1):
    s+=str(i)
for i in permutations(s):
    l.append(i)
for i in range(len(l)):
   if(i==k-1):
       print("".join(l[i]))