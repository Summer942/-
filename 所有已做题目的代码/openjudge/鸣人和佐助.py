from collections import deque
M,N,T=map(int,input().split())
board=[]
for _ in range(M):
    line=input()
    board.append(line)
    if '@' in line:
        sx,sy=_,line.index('@')
queue=deque([(sx,sy,T,0)])
visited={(sx,sy,T)}
flag=False
while queue:
    x,y,T,time=queue.popleft()
    if board[x][y]=='+':
        flag=True
        break
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if board[nx][ny]=='#':
            if T>0 and (nx,ny,T-1) not in visited:
                queue.append((nx,ny,T-1,time+1))
                visited.add((nx,ny,T-1))
        elif (nx,ny,T) not in visited:
            queue.append((nx,ny,T,time+1))
            visited.add((nx,ny,T))
if flag:
    print(time)
else:
    print(-1)