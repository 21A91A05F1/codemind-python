s=input()
k=[]
c=0
for i in range(0,len(s)):
    flag=0
    for j in range(0,len(s)):
        if(s[i]==s[j] and i!=j):
            flag=1
            break
            
    else:
        c+=1
        print(s[i])
        break
if(c==0):
    print("-1")