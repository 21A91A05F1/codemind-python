n=int(input())
arr=list(map(int,input().split()))
if(len(set(arr))==1):
    print("0")
else:
    c=0
    l=[]
    for i in range(n):
        c=0
        for j in range(i,n):
            if(arr[i]==arr[j]):
                c+=1
                l.append(c)
    print(max(l))
                