n=int(input())
arr=list(map(int,input().split()))
s=0
l=[]
for i in arr:
    s+=i
for i in arr:
    if(s%i==0):
        l.append(i)
print(max(l))
        