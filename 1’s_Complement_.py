n=int(input())
s=bin(n)[2:]
l=''
for i in s:
    if(i=='1'):
        l+='0'
    else:
        l+='1'
print(int(l,2))
    
    