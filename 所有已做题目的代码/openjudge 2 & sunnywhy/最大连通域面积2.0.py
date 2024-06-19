def dfs(a,b,graph,visited):
    if a<0 or b<0 or a>=N or b>=M:
        return 0
    if graph[a][b]!='W'or visited[a][b]:
        return 0
    visited[a][b]=True
    area=1
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx==dy==0:
                continue
            area+=dfs(a+dx,b+dy,graph,visited)
    return area
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    graph=[input() for i in range(N)]
    visited=[[False]*M for i in range(N)]
    max_area=0
    for x in range(N):
        for y in range(M):
            area=dfs(x,y,graph,visited)
            max_area=max(area,max_area)
    print(max_area)