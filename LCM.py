n1,n2=map(int,input().split())
if(n1>n2):
    max=n1
else:
    max=n2
while(1):
    if(max%n1==0 and max%n2==0):
        print(max)
        break
    max+=1