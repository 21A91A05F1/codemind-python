n=int(input())
k=list(map(int,input().split()))
s=[]
for i in k:
    s.append(len(str(i)))
for i in k:
    if(len(str(i))==max(s)):
        print(i,end=" ")
    