from collections import deque
#BFS
def bfs(start,end,board,w,h):
    queue=deque([start]) #起点位置、线段方向、线段个数进入队列
    visited=set() #记录已经过位置与线段方向
    ans=[] #记录线段条数
    directions=[(-1,0),(1,0),(0,-1),(0,1)] #四个移动方向：上下左右
    while queue: #有路可走时
        x,y,direction,segment=queue.popleft() 
        if (x,y)==end: #特判：两卡片重合
            ans.append(segment)
            break
        for i,(dx,dy) in enumerate(directions):
            nx,ny=x+dx,y+dy #移动后的坐标
            if 0<=nx<(h+2) and 0<=ny<(w+2) and ((nx,ny,i) not in visited): #排除越界和重复经过的情况
                direction_=i #用索引表示移动方向
                if direction_!=direction: #若方向不同说明线段数加1
                    segment_=segment+1
                else:
                    segment_=segment
                if (nx,ny)==end: #到达终点
                    ans.append(segment_)
                    continue #continue而非break：通过别的路也可能到终点且线段数更少
                if board[nx][ny]!='X':
                    visited.add((nx,ny,i)) 
                    queue.append((nx,ny,direction_,segment_))
    if len(ans)==0: #不能到达
        return -1
    else:
        return min(ans)
board_num=0
while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    board_num+=1
    print('Board #{}:'.format(board_num))
    board=[' '*(w+2)]+[' '+input()+' 'for _ in range(h)]+[' '*(w+2)] #由于可以出矩形板，需要多加一圈
    pair_num=0
    while True:
        y1,x1,y2,x2=map(int,input().split())
        if x1==y1==x2==y2==0:
            break
        pair_num+=1
        start=(x1,y1,-1,0) #-1的作用：刚开始无论走哪个方向都会产生新线段
        end=(x2,y2)
        segment=bfs(start,end,board,w,h)
        if segment==-1:
            print('Pair {}: impossible.'.format(pair_num))
        else:
            print('Pair {}: {} segments.'.format(pair_num,segment))
    print() 