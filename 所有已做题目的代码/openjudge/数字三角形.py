n=int(input())
triangle=[]
for i in range(n):
    triangle.append(list(map(int,input().split())))
for ii in range(1,n):
    for iii in range(ii+1):
        if iii==0:
            triangle[ii][iii]=triangle[ii][iii]+triangle[ii-1][iii]
        elif iii==ii:
            triangle[ii][iii]=triangle[ii][iii]+triangle[ii-1][iii-1]
        else:
            triangle[ii][iii]=triangle[ii][iii]+max(triangle[ii-1][iii],triangle[ii-1][iii-1])
print(max(triangle[n-1]))