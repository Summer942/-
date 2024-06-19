N=int(input())
str=input()
x,y=0,0
for i in range(N):
    if str[i]=='A':
        x+=1
    else:
        y+=1
if x>y:
    print('Anton')
elif x==y:
    print('Friendship')
else:
    print('Danik')