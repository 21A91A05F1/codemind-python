t=int(input())
while(t):
    flag=0
    n=input()
    
    for i in range(0,len(n)):
        if(n[i]<='9' and n[i]>='0'):
            flag=flag+1
    if(flag==len(n)):
        print("True")
    else:
        print("False")
    t=t-1