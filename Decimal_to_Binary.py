n=int(input())
while(n):
    k=int(input())
    p=bin(k)
    #p=p[2]
    print(p.replace("0b",""))
    n-=1