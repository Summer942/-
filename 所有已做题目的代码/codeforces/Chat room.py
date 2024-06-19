greeting=input()
a=int(greeting.find('h'))
b=int(greeting.find('e',a+1))
c=int(greeting.find('l',b+1))
d=int(greeting.find('l',c+1))
e=int(greeting.find('o',d+1))
if a==-1 or b==-1 or c==-1 or d==-1 or e==-1:
    print('NO')
else:
    print('YES')