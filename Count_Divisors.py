a,b,c=map(int,input().split())

d=0
for a in range (a,b+1):
    if(a%c==0):
        d=d+1
print (d)
    