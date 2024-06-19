n,m,k=map(int,input().split())
matrix=[[0]*(m+2) for i in range(n+2)]
z=0
for i in range(k):
    x,y=map(int,input().split())
    matrix[x-1][y-1]=1
    if matrix[x-2][y-2]==matrix[x-1][y-2]==matrix[x-2][y-1]==1\
    or matrix[x-1][y]==matrix[x-2][y-1]==matrix[x-2][y]==1\
    or matrix[x-1][y-2]==matrix[x][y-1]==matrix[x][y-2]==1\
    or matrix[x][y]==matrix[x][y-1]==matrix[x-1][y]==1:
        z=i+1
        break
print(z)