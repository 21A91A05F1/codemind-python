s=input()
v="aeiouAEIOU"
c,d=0,0
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if s[j] in v:
            c+=1
            if(d<c):
                d=c
        else:
            break
print(d)
      