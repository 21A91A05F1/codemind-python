s=input()
u=d=r=l=0
for i in s:
    if i=="U":
        u+=1
    elif i=="D":
        d+=1
    elif i=="L":
        l+=1
    elif i=="R":
        r+=1
if(l==r and u==d):
    print("True")
else:
    print("False")
        
    