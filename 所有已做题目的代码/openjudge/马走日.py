def dfs(n,m,x,y,visited,count):
    ans=0
    if x<0 or x>n-1 or y<0 or y>m-1 or visited[x][y]:
        return 0
    visited[x][y]=True
    if count==n*m-1:
        visited[x][y]=False
        return 1
    for (dx,dy) in [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]:
        ans+=dfs(n,m,x+dx,y+dy,visited,count+1)
    visited[x][y]=False
    return ans
T=int(input())
for _ in range(T):
    n,m,x,y=map(int,input().split())
    visited=[[False]*m for i in range(n)]
    ans=dfs(n,m,x,y,visited,0)
    print(ans)