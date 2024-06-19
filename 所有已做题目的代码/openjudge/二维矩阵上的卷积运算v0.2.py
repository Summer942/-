m,n,p,q=map(int,input().split())
matrix=[list(map(int,input().split())) for i in range(m)]
convolution_core=[list(map(int,input().split())) for ii in range(p)]
result=[[0]*(n+1-q) for iii in range(m+1-p)]
for x in range(m+1-p):
    for y in range(n+1-q):
        number=0
        for a in range(p):
            for b in range(q):
                number+=matrix[x+a][y+b]*convolution_core[a][b]
        result[x][y]=str(number)
for _ in result:
    print(' '.join(_))
    
