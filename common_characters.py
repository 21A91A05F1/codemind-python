s=input().lower()
p=input().lower()
r=""
for i in s:
    if i!=" ":
        if i in p:
            if i not in r:
                   r+=i
k=sorted(r)
if len(r):
    print("".join(k))
else:
    print("-1")
