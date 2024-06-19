from collections import defaultdict
n,m,l=map(int,input().split())
pictures=defaultdict(list)
for i in range(m):
    a,b=map(int,input().split())
    pictures[a].append(b)
    pictures[b].append(a)
for ii in pictures.keys():
    pictures[ii].sort()
start=int(input())
visited=set()
ans=[]
def dfs(x,d):
    if d>l:
        return
    if x in visited:
        return
    visited.add(x)
    ans.append(x)
    if x not in pictures.keys():
        return
    for y in pictures[x]:
        dfs(y,d+1)
dfs(start,0)
print(' '.join(map(str,ans)))