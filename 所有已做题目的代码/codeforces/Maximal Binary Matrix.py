n,k=map(int,input().split())
if n**2<k:
    print(-1)
else:
    matrix=[[str(0)]*n for i in range(n)]
    a=0
    while k!=0:
        k-=1
        matrix[a][a]=str(1)
        l=a+1
        while k>1 and l<n:
            k-=2
            matrix[a][l]=matrix[l][a]=str(1)
            l+=1
        a+=1
    for i in matrix:
        print(' '.join(i))