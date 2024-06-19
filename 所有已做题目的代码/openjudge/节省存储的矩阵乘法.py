n,m1,m2=map(int,input().split())
matrixA=[[0]*n for a in range(n)]
matrixB=[[0]*n for b in range(n)]
for i in range(m1):
    x1,y1,element1=map(int,input().split())
    matrixA[x1][y1]=element1
for ii in range(m2):
    x2,y2,element2=map(int,input().split())
    matrixB[x2][y2]=element2
for j in range(n):
    for k in range(n):
        element_j_k=0
        for l in range(n): 
            element_j_k+=matrixA[j][l]*matrixB[l][k]
        if element_j_k!=0: 
            print(j,k,element_j_k)