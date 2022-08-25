x=int(input())
def fun(x):
    rev=0
    while(x):
        d=x%10
        rev=rev*10+d
        x//=10
    return rev

while(x):
    x=x+fun(x)
    if(x==fun(x)):
        print(x)
        break

