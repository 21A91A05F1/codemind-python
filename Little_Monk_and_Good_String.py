s=input()
c=0
k=[]
v="aeiouAEIOU"
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
            if s[j] in v:
                c+=1
                k.append(c)
            else:
                break
print(max(k))
            
   