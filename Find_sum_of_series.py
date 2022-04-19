n=int(input(""))
i=1
res=0
while i<=n:
    res=res+(1/i)
    i=i+1
c="{:.2f}".format(res)
print(c)