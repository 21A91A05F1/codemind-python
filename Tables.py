n,m=map(int,input().split())
i=1
while i<=m:
    if i%2!=0:
        print('{0} x {1} = {2}'.format(n,i,n*i))
    i+=1
    

