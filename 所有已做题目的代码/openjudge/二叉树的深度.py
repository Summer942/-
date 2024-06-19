class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def build_tree(n,nodes):
    dic={i:TreeNode(i)for i in range(1,n+1)}
    for i,(left,right) in enumerate(nodes,start=1):
        if left!=-1:
            dic[i].left=dic[left]
        if right!=-1:
            dic[i].right=dic[right]
    return dic[1]
def max_depth(root):
    if root is None:
        return 0
    else:
        left_depth=max_depth(root.left)
        right_depth=max_depth(root.right)
        return max(left_depth,right_depth)+1
n=int(input())
nodes=[]
for _ in range(n):
    left,right=map(int,input().split())
    nodes.append((left,right))
root=build_tree(n,nodes)
print(max_depth(root))