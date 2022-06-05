n=int(input())
while(n):
    k=int(input())
    arr=list(map(int,input().split()))
    i=0
    while(i+1<=len(arr)):
        arr.insert(i,arr[-1])
        arr.pop()
        i+=2
    print(*arr)

    n=n-1