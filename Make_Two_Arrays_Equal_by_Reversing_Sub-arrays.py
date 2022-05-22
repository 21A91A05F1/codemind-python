n=int(input())
k=list(map(int,input().split()))
p=int(input())
l=list(map(int,input().split()))
if(sorted(k)==sorted(l)):
    print("True")
else:
    print("False")