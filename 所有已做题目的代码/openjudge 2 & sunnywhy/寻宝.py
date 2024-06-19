from collections import deque
m,n=map(int,input().split())
treasure_map=[list(map(int,input().split()))for _ in range(m)]
visited=[[False]*n for _ in range(m)] #记录是否经过
step=[[0]*n for _ in range(m)] #记录走到该格所需最少步数
#上下左右四个移动方向
dx=[0,0,-1,1]
dy=[1,-1,0,0]
#起点进入路线并初始化 
way=deque([(0,0)])
visited[0][0]=True
step[0][0]=0
flag=0 #标记是否拿到宝藏
if treasure_map[0][0]==1: #特判：起点就拿到宝藏
    flag=1
    print(0)
else:
    while way: #有路可走时
        x,y=way.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i] #尝试移动
            if 0<=nx<m and 0<=ny<n and treasure_map[nx][ny]!=2 and not visited[nx][ny]: #排除越界，重复经过，陷阱
                visited[nx][ny]=True
                step[nx][ny]=step[x][y]+1
                way.append((nx,ny))
                if treasure_map[nx][ny]==1: #拿到宝藏
                    flag=1
                    print(step[nx][ny])
if flag==0: #拿不到宝藏
    print('NO')
