n=list(map(str,input().split()))
for i in n:
    print(ord(max(i))-ord(min(i)),end=' ')