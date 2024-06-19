def find(i): #寻找根节点
    if parent[i]!=i: #如果当前节点的根节点不是自己
        parent[i]=find(parent[i])
    return parent[i]
def union(x,y): #使y的根节点成为x的根节点的根节点
    parent[find(x)]=find(y)
i=0
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    i+=1
    parent=list(range(n+1)) #初始化每个结点的根节点为自己
    for _ in range(m):
        a,b=map(int,input().split())
        union(a,b)
    religions=set(find(x) for x in range(1,n+1))
    print('Case '+format(i)+': '+format(len(religions)))