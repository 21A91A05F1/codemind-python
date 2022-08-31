from math import sqrt
def is_prime(n):
    if n==1:
        return 0
   
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
for i in range(n):
    if(is_prime(n-i)==1 and is_prime(n+i)==1):
        print(i)
        break
    elif(is_prime(n-i)==1):
        print(i)
        break
    elif(is_prime(n+i)==1):
        print(i)
        break
    