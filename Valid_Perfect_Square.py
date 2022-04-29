t=int(input())
while(t>0):
    n=int(input())
    a=n**(1/2)
    if(int (a)*a==n):
        print("True")
    else:
        print("False")
    t=t-1