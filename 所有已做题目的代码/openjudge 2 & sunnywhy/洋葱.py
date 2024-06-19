n=int(input())
matrix=[list(map(int,(input().split())))for _ in range(n)]
res=[]
for i in range((n+1)//2):
    total=0
    for j in range(i,n-i-1):
        total+=matrix[i][j]+matrix[j][n-1-i]+matrix[-j-1][i]+matrix[-i-1][-1-j]
    res.append(total)
if n%2!=0:
    res.append(matrix[(n-1)//2][(n-1)//2])
print(max(res))
