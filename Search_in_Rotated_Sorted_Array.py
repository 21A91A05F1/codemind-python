n=int(input())
p=list(map(int,input().split()))
k=int(input())
for i in range(len(p)):
    if(p[i]==k):
        print((i))
        break
else:
    print("-1")