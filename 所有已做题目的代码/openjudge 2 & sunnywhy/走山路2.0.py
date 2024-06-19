import heapq
m,n,p=map(int,input().split())
board=[list((input().split()))for _ in range(m)]
for _ in range(p):
    flag=False
    sx,sy,ex,ey=map(int,input().split())
    if board[sx][sy]=='#' or board[ex][ey]=='#':
        print('NO')
        continue
    visited=[[False]*n for _ in range(m)]
    heap=[]
    heapq.heappush(heap,(0,sx,sy))
    while heap:
        energy,x,y=heapq.heappop(heap)
        if x==ex and y==ey:
            flag=True
            break
        visited[x][y]=True
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=dx+x,dy+y
            if nx<0 or nx>=m or ny<0 or ny>=n or visited[nx][ny] or board[nx][ny]=='#':
                continue
            heapq.heappush(heap,(energy+abs(int(board[x][y])-int(board[nx][ny])),nx,ny))
    if flag:
        print(energy)
    else:
        print('NO')
        