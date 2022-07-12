n=input()
k=[]
c=0
for i in n:
    if i in "aeiou":
        if i not in k:
            k.append(i)
            c+=1
if(len(k)==5):
    print("True")
else:
    print("False")
        
        