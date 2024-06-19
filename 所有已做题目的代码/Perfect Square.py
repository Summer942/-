t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    matrix=[input() for ii in range(n)]
    num=0
    for j in range(n//2):
        left=top=j
        right=bottom=n-1-j
        for jj in range(n-1-2*j):
            a=ord(matrix[top][left+jj])
            b=ord(matrix[top+jj][right])
            c=ord(matrix[bottom][right-jj])
            d=ord(matrix[bottom-jj][left])
            e=max(a,b,c,d)
            f=4*e-a-b-c-d
            num+=f
    ans.append(num)
for _ in ans:
    print(_)