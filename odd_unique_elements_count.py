n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i not in s and i%2==1:
        s.append(i)
print(len(s))