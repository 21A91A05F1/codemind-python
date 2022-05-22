p=input()
c1=0
c2=0
for i in range(0,len(p)):
    c1=0
    for j in range(len(p)):
        if(p[i]==p[j]):
            c1=c1+1
    if(c1==1):
        print(i)
        break
    else:
        c2=c2+1
if(c2==len(p)):
    print("-1")
            
    