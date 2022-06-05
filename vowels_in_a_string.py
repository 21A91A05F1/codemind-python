s=input()
k=input()
c=0
for i in range(len(s)):
    if (s[i]==k):
        c=1
        print("True")
        print(i)
        break
       
if(c==0):
    print("False")