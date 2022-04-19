n=int(input(""))
i=0
rev=0
temp=n
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if rev==temp:
    print ("True")
else:
    print("False")
