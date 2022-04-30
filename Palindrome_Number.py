t=int(input())

while(t>0):
    n=int(input())
    rev=0
    p=n
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
   
  
    if(rev==p):
        print("True")
    else:
        print("False")
        rev=0
    t=t-1