from collections import deque
class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
N=int(input())
nodes={i:Treenode(i)for i in range(1,N+1)}
for i in range(1,N+1):
    a,b=map(int,input().split())
    if a!=-1:
        nodes[i].left=nodes[a]
    if b!=-1:
        nodes[i].right=nodes[b]
ans=[]
node=nodes[1]
queue=deque([node])
while queue:
    level_size=len(queue)
    for i in range(level_size):
        node=queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    ans.append(node.value)
print(*ans)
