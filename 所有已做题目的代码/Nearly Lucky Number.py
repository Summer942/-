n=input()
x=0
for i in range(len(n)):
    if n[i]=='4' or n[i]=='7':
        x=x+1
    else:
        x=x
if x==4 or x==7:
    print('YES')
else:
    print('NO')
    
    