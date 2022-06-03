n=input()
s="aeiou"
b=[]
for i in range(len(n)):
    if n[i] in s:
        b.append(n[i])
c=0
for i in range(len(s)):
    if s[i] not in b:
        print(s[i],end=" ")
    else:
        c+=1
if(c==5):
    print(0)
        
        