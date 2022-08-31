n=int(input())
k=list(map(int,input().split()))
c=d=e=0
for i in range(len(k)):
    c=1
    for j in range(i,len(k)):
        if(k[i]==k[j]):
            c+=1
    if(c>d):
        d=c
        e=k[i]
    elif(c==d):
        d=c #if many numbers have same frequency,
            #then print the smallest one
        if(k[i]<e):
            e=k[i]
print(e)
        