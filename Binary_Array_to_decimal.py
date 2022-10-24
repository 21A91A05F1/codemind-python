n=int(input())
k=list(map(int,input().split()))
s=''
for i in k:
    s+=str(i)
print(int(s,2))