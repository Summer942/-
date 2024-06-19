from collections import deque
n=int(input())
maze=[list(map(int,input().split()))for _ in range(n)]
count=0
for i in range(n):
    for j in range(n):
        if count==0 and maze[i][j]==5:
            x1,y1=i,j
            count=1
        elif count==1 and maze[i][j]==5:
            x2,y2=i,j
            break
queue=deque([(x1,y1,x2,y2)])
visited=set()
directions=[(1,0),(-1,0),(0,1),(0,-1)]
flag=0
while queue:
    x,y,xx,yy=queue.popleft()
    if maze[x][y]==9 or maze[xx][yy]==9:
        flag=1
        break
    if (x,y,xx,yy) in visited:
        continue
    visited.add((x,y,xx,yy))
    for (dx,dy) in directions:
        nx,ny,nxx,nyy=dx+x,dy+y,dx+xx,dy+yy
        if 0<=nx<n and 0<=ny<n and 0<=nxx<n and 0<=nyy<n and (nx,ny,nxx,nyy) not in visited:
            if maze[nx][ny]!=1 and maze[nxx][nyy]!=1:
               queue.append((nx,ny,nxx,nyy))
if flag==0:
    print('no')
else:
    print('yes')
    

