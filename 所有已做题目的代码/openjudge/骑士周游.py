def knight_tour(n,sr,sc):
    visited=[[False]*n for _ in range(n)]
    moves=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    def is_valid_move(r,c):
        return 0<=r<n and 0<=c<n and not visited[r][c]
    def count_valid_move(r,c):
        count=0
        for dr,dc in moves:
            nr,nc=dr+r,dc+c
            if is_valid_move(nr,nc):
                count+=1
        return count
    def get_next_move(r,c):
        min_count=9
        next_move=None
        for dr,dc in moves:
            nr,nc=dr+r,dc+c
            if is_valid_move(nr,nc):
                count=count_valid_move(nr,nc)
                if count<min_count:
                    min_count=count
                    next_move=(nr,nc)
        return next_move
    def dfs(r,c,count):
        visited[r][c]=True
        count+=1
        if count==n*n:
            return True
        next_move=get_next_move(r,c)
        if next_move:
            nr,nc=next_move
            if dfs(nr,nc,count):
                return True
        visited[r][c]=False
        return False
    return 'success' if dfs(sr,sc,0) else 'fail'
n=int(input())
sr,sc=map(int,input().split())
print(knight_tour(n,sr,sc))