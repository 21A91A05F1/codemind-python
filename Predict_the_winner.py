n=int(input())
k=list(map(int,input().split()))
s1,s2=0,0
for i in range(len(k)):
    if(i%2==0):
        s1+=k[i]
    else:
        s2+=k[i]
res=(abs(s2-s1))
if((res)%4==0):
    print("X")
else:
    print("Y")