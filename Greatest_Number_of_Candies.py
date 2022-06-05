n=int(input())
k=list(map(int,input().split()))
m=int(input())
v=max(k)
for i in range(n):
    if k[i]+m>=v:
        print("True",end=" ")
    else:
        print("False",end=" ")