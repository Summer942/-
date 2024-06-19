n,m=map(int,input().split())
island=[[0]*(m+2)]
for i in range(n): 
    island.append([0]+list(map(int,input().split()))+[0])
island.append([0]*(m+2))
z=0
for x in range(1,n+1):
    for y in range(1,m+1):
        if island[x][y]==1:
            if island[x][y-1]==0:
                z+=1
            if island[x][y+1]==0:
                z+=1
            if island[x-1][y]==0:
                z+=1
            if island[x+1][y]==0:
                z+=1 
print(z)