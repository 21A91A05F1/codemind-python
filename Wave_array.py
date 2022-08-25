n=int(input())
l=list(map(int,input().split()))
c=0
if l[0]>l[1]:
    for i in range(n-1):
        if(i%2==0 and l[i]>l[i+1]):
            c+=1
        if(i%2==1 and l[i]<l[i+1]):
            c+=1
    if(c==n-1):
        print("yes")
    else:
        print("no")
else:
    for i in range(n-1):
        if(i%2==0 and l[i]<l[i+1]):
            c+=1
        if(i%2==1 and l[i]>l[i+1]):
            c+=1
    if(c==n-1):
        print("yes")
    else:
        print("no")
    
            
