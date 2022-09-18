s=input()
m=1
c=1
k=[]
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        c+=1
        if(m<c):
            m=c
    else:
        c=1
print(m)
       