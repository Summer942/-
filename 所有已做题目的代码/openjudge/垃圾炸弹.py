matrix=[[0]*1025 for _ in range(1025)]
d=int(input())
n=int(input())
for ii in range(n):
    x,y,i=map(int,input().split())
    for m in range(max(0,x-d),min(1025,x+d+1)):
        for n in range(max(0,y-d),min(1025,y+d+1)):
            matrix[m][n]+=i
rubish=ans=0
for a in range(1025):
    for b in range(1025):
        if matrix[a][b]>rubish:
            rubish=matrix[a][b]
            ans=1
        elif matrix[a][b]==rubish:
            ans+=1
print(ans,rubish)