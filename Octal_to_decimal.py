def o_t_d(n):
    temp=n
    res=0
    base=1
    while(temp!=0):
        d=temp%10 
        temp//=10
        res+=(d*base)
        base*=8
    return res
n=int(input())
print(o_t_d(n))
