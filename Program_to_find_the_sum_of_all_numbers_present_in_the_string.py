n=input()
i=0
sum=0
for i in n:
    if(i.isnumeric()):
        sum=sum+int(i)
        
print(sum)