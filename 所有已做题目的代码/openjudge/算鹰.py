board=[input()for _ in range(10)]
visited=[[False]*10 for _ in range(10)]
def dfs(x,y,board,visited):
    if x<0 or x>=10 or y<0 or y>=10 or board[x][y]=='-' or visited[x][y]:
        return 
    visited[x][y]=True
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=dx+x,dy+y
        dfs(nx,ny,board,visited)
    return    
ans=0
for x in range(10):
    for y in range(10):
        if not visited[x][y] and board[x][y]=='.':
            dfs(x,y,board,visited)
            ans+=1
print(ans)

        
        
