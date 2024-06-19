string=input()
a=string.find('h')
b=string.find('e',a+1)
c=string.find('l',b+1)
d=string.find('l',c+1)
e=string.find('o',d+1)
if a==-1 or b==-1 or c==-1 or d==-1 or e==-1:
    print('NO')
else:
    print('YES')

