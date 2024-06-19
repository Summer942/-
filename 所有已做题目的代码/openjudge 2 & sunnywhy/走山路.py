import heapq
def bfs(start,end,map_,n,m):
    heap=[]
    visited=set()
    ans=[]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    heapq.heappush(heap, start)
    while heap:
        step,x,y=heapq.heappop(heap)
        visited.add((x,y))
        if (x,y)==end:
            ans.append(step)
        for (dx,dy) in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and ((nx,ny) not in visited) and map_[nx][ny]!='#':
                step_=step+abs(int(map_[x][y])-int(map_[nx][ny]))
                heapq.heappush(heap,(step_,nx,ny))
    if ans:
        return min(ans)
    else:
        return 'NO'
m,n,p=map(int,input().split())
map_=[list(input().split())for _ in range(m)]
for i in range(p):
    x1,y1,x2,y2=map(int,input().split())
    start=(0,x1,y1)
    end=(x2,y2)
    if map_[x1][y1]=='#' or map_[x2][y2]=='#':
        print('NO')
    else:    
        print(bfs(start,end,map_,n,m))