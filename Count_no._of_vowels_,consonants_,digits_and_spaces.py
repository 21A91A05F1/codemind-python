s=input()
v,c,d,w=0,0,0,0
for i in range(0,len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        v+=1
    if(s[i]>='0' and s[i]<='9'):
        d+=1
    if(s[i]==' '):
        w+=1
c=len(s)-(v+d+w)
print("Vowels: {}
Consonants: {}
Digits: {}
White spaces: {}".format(v,c,d,w))