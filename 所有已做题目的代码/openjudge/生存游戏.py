#读取输入，列表推导式形成矩阵
n,m=map(int,input().split())
cells=[list(map(int,input().split())) for i in range(n)]
#为矩阵套上一层保护圈，防止索引越界
cells.insert(0,[0]*(m+2))
cells.append([0]*(m+2))
for ii in range(1,n+1):
    cells[ii].insert(0,0)
    cells[ii].append(0)
#新矩阵，根据题目要求不能在原矩阵中修改元素
cells_new=[[0]*(m+2) for ii in range(n+2)]
#计算每个细胞周围活细胞的数量，并根据题目要求判断
for x in range(1,n+1):
    for y in range(1,m+1):
        livingcells=cells[x-1][y-1]+cells[x-1][y]+cells[x-1][y+1]+\
                    cells[x+1][y-1]+cells[x+1][y]+cells[x+1][y+1]+\
                    cells[x][y-1]+cells[x][y+1]
        if cells[x][y]==1 and (livingcells<2 or livingcells>3):
            cells_new[x][y]=str(0)
        elif cells[x][y]==1 and 2<=livingcells<=3:
            cells_new[x][y]=str(1)
        elif cells[x][y]==0 and livingcells==3:
            cells_new[x][y]=str(1)
        else:
            cells_new[x][y]=str(0)
#把新矩阵的保护圈删掉，得到输出
del cells_new[0]
del cells_new[-1]
for iii in range(n):
    del cells_new[iii][0]
    del cells_new[iii][-1]
for _ in cells_new:
    print(' '.join(_))
 
