n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    c=0
    for j in range(i+1,n):
        if l[j]>l[i]:
            print(j-i,end=" ")
            c=1
            break
    if(c==0):
        print("0",end=" ")