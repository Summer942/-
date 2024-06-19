matrixs=[list(map(int,input().split())) for i in range(5)]
maxs=[]
mins=[]
for ii in range(5):
    matrix=matrixs[ii]
    a=max(matrix)
    y=matrix.index(a)
    maxs.append([ii+1,y+1,a])
for iii in range(5):
    c=0
    x=0
    b=matrixs[c][iii]
    while c<=3: 
        if b<matrixs[c+1][iii]:
            b=b
            x=x
        else:
            b=matrixs[c+1][iii]
            x=c+1
        c+=1
    mins.append([x+1,iii+1,b])
z=0
for _ in maxs:
    if _ in mins:
        z=1
        print(' '.join(map(str,_)))
if z!=1:
    print('not found')