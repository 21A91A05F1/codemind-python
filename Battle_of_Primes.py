n=int(input())
m=int(input())
s1=n+m
c=0
for i in range(1,11):
    s2=s1+i
    for j in range(2,s2):
        if(s2%j==0):
            break
    else:
        print(i)
        break