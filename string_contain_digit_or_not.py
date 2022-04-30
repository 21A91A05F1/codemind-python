n=input()
i=0


c=0
for i in n:
    if(i>='0' and i<='9' ):
        c=c+1
if(c>0):
    print("Contains %d digit"%c)
else:
    print("Doesn't contain digit")
            
    
    