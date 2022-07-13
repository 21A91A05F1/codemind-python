n=int(input())
k=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if(i!=j):
            if(k[i]>k[j]):
                c+=1
    print(c,end=" ")