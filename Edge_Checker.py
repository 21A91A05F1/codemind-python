a,b=map(int,input().split())
if(abs(a-b)==1 or abs(b-a)==1):
    print("Yes")
elif((a==1 and b==10) or(a==10 and b==1)):
    print("Yes")
else:
    print("No")