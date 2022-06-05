k=list(map(str,input().lower().split()))
p=[]
k="".join(k)
k=set(k)
k=sorted(k)
p="".join(k)
p=p.replace(" ","")
print(len(p))