def balanced(l,n):
    for i in range(0,n):
        s1=sum(l[0:i])
        s2=sum(l[i+1:])
        if(s1==s2):
            return 1
    else:
        return 0
        
t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(balanced(l,n)):
        print("YES")
    else:
        print("NO")
    t-=1 