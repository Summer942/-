def dfs(board,a,b,visited):
    if a<0 or a>=N or b<0 or b>=M:    
        return 0
    elif visited[a][b] or board[a][b]!='W':
        return 0
    visited[a][b]=True
    area=1
    for c in [-1,0,1]:
        for d in [-1,0,1]:
            if c==0 and d==0:
                continue
            area+=dfs(board, a+c, b+d, visited)
    return area
ans=[]
for i in range(int(input())):
    N,M=map(int,input().split())
    board=[input() for ii in range(N)]
    visited=[[False]*M for iii in range(N)]
    max_area=0
    for x in range(N):
        for y in range(M):
            if not visited[x][y] and board[x][y]=='W':
                area=dfs(board,x,y,visited)
                max_area=max(area,max_area)
    ans.append(max_area)
for _ in ans: 
    print(_)