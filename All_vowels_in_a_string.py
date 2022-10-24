s=input()
v='aeiou'
l=''
for i in s:
    if i in v:
        if i not in l:
            l+=i
if(len(l)==5):
    print("True")
else:
    print("False")
    
    