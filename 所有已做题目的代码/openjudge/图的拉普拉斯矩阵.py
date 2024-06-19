n,m=map(int,input().split())
matrix_D=[[0]*n for i in range(n)]
matrix_A=[[0]*n for ii in range(n)]
matrix_L=[[0]*n for iii in range(n)]
number=[]
for j in range(m):
    a,b=map(int,input().split())
    matrix_A[a][b]=matrix_A[b][a]=1
    number.append(a)
    number.append(b)
for jj in range(n):
    matrix_D[jj][jj]=number.count(jj)
for x in range(n):
    for y in range(n):
        matrix_L[x][y]=str(matrix_D[x][y]-matrix_A[x][y])
for _ in matrix_L:
    print(' '.join(_))
    