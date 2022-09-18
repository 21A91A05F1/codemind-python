s=input()
b=s.count('b')
a=s.count('a')
l=s.count('l')
o=s.count('o')
n=s.count('n')
m=min(b,a,l//2,o//2,n)
if(b==0 or a==0 or l==0 or o==0 or n==0):
        print("0")
else:
    print(m)
           
            
