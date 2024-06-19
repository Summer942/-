class Treenode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def build_tree(n,nodes):
    dic={i:Treenode(i)for i in range(n)}
    for i,(left,right) in enumerate(nodes):
        if left!=-1:
            dic[i].left=dic[left]
        if right!=-1:
            dic[i].right=dic[right]
    return dic
def max_height(root):
    if root is None:
        return -1
    else:
        left_height=max_height(root.left)
        right_height=max_height(root.right)
        return max(left_height,right_height)+1
n=int(input())
nodes=[]
count=0
for _ in range(n):
    left,right=map(int,input().split())
    nodes.append((left,right))
    if left==right==-1:
        count+=1
dic=build_tree(n,nodes)
height=0
for i in range(n):
    root=dic[i]
    height=max(max_height(root),height)
print(height,count)