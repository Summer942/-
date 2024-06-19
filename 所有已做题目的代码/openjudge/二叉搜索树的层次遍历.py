from collections import deque
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,key):
    if not root:
        return Treenode(key)
    if root.val>key:
        root.left=insert(root.left,key)
    if root.val<key:
        root.right=insert(root.right,key)
    return root
def level_order_traversal(root):
    result=[]
    queue=deque([root])
    while queue:
        node=queue.popleft()
        result.append(node.val)
        if node.left:
           queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
root=None
keys=list(map(int,input().split()))
for key in keys:
    root=insert(root,key)
print(' '.join(map(str,level_order_traversal(root))))