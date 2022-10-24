s=input()
v='aeiouAEIOU'
c=0
for i in range(len(s)):
        if s[i] not in v and s[i]!=' 'and s[len(s)-1-i] in v:
            c+=1
print(c)