def bal(s):
    while True:
        if '()'in s:
             s=s.replace('()','')
        elif '{}' in s:
            s=s.replace('{}','')
        elif '[]' in s:
            s=s.replace('[]','')
        else:
            return not s
s=input()
print(bal(s))