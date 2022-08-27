t=int(input())
while(t):
    n=int(input())
    s=input()
    c=0
    k=[]
    for i in range(len(s)):
        c=0
        for j in range(len(s)):
            if(s[i]==s[j] and i!=j):
                c=1
                break
        if(c==0):
            k.append(s[i])
            break
    if(len(k)!=0):
        print(*k)
    else:
        print("-1")
            
    t-=1