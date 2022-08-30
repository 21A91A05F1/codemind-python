n=int(input())
r=''
while(n>0):
    r=chr(ord('A')+(n-1)%26)+r
    n=(n-1)//26
print(r)