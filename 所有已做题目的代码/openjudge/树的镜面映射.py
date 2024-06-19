from collections import deque
class Treenode:
    def __init__(self,value,type_):
        self.value=value
        self.left=None
        self.right=None
        self.type=type_
def build_tree(n,prefix):
    stack=[] #存储还没有孩子子节点的双亲节点
    root=Treenode(prefix[0][0],prefix[0][1])
    stack.append(root)
    for i in range(1,n):
        node=Treenode(prefix[i][0],prefix[i][1])
        if stack[-1].left is None: #栈顶双亲节点没有左子节点
            stack[-1].left=node
        else: 
            while stack[-1].right is not None: #若栈顶双亲节点已有左右两个子节点，则出栈
                stack.pop()
            stack[-1].right=node
        if node.type=='0': #内部节点有子节点，需入栈
            stack.append(node)
    return root
def traversal(root): 
    queue=deque()
    stack=deque()
    while root and root.value!='$': 
        stack.append(root)
        root=root.right
    while stack:
        queue.append(stack.pop())
    while queue:
        root=queue.popleft()
        print(root.value,end=' ')
        if root.left and root.left.value!='$':
            root=root.left
            while root and root.value!='$': 
                stack.append(root)
                root=root.right
            while stack:
                queue.append(stack.pop())
n=int(input())
prefix=input().split()
root=build_tree(n,prefix)
traversal(root)
