n=int(input())
k=list(map(int,input().split()))
p=list(map(int,input().split()))
s1,s2=0,0
for i in k:
    s1+=i
for i in p:
    s2+=i
if(s1>s2):
    print("0")
else:
    print(s2-s1)
