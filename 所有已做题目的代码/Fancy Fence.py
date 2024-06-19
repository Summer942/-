angle=[]
for i in range(3,361):
    if 360%i==0:
       angle.append(180-360//i) 
t=int(input())
for ii in range(t):
    a=int(input())
    if a in angle:
        print('YES')
    else:
        print('NO')


