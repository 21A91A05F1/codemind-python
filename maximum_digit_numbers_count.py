n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    i=str(i)
    b+=[len(i)]
for i in a:
    i=str(i)
    if(len(i)==max(b)):
        print(i,end=' ')