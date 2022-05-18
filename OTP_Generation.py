n=int(input())
rev=0
while(n):
    d=n%10
    rev=rev*10+d
    n=n//10
while(rev):
    d2=rev%10
    rev=rev//10
    if(d2%2==0):
        continue
    else:
        print(d2*d2,end='')
    
    