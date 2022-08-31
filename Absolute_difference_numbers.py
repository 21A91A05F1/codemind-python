n,k=map(int,input().split())
s=str(n)
a=s[-k:]
b=s[:k]
a=int(a)
b=int(b)
print(abs(a-b))