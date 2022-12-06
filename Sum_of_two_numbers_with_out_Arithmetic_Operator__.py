a,b=map(int,input().split())
while(b!=0):
    c=a&b
    a^=b
    b=c<<1
print(a)