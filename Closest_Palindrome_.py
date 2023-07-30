def ispali(s):
    temp=s
    rev=0
    while(s!=0):
        d=s%10
        rev=rev*10+d
        s=s//10
    if(rev==temp):
        return 1
    else:
        return 0
n=int(input())
for i in range(1,10000):
    if(ispali(n+i)):
        m=n+i
        break
for i in range(1,10000):
    if(ispali(n-i)):
        p=n-i
        break
if(n-p==m-n):
    print(p,m)
elif(n-p>m-n):
    print(m)
else:
    print(p)
