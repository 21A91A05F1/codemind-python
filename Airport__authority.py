n=int(input())
arr=[]
for j in range(n):
    a=int(input())
    arr.append(a)
t=int(input())
s=0
for i in range(n):
    if(arr[i]>t):
        s=s+2
    else:
        s=s+1
print(s)
        
    
    