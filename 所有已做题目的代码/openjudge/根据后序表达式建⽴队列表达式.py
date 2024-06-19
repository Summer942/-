from collections import deque
class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def build_tree(postfix):
    stack=[]
    for char in postfix:
        if char.islower():
            node=Treenode(char)
            stack.append(node)
        else:
            right=stack.pop()
            left=stack.pop()
            new_node=Treenode(char)
            new_node.left=left
            new_node.right=right
            stack.append(new_node)
    return stack[0]
def level_traversal(root):
    result=[]
    if not root:
        return result
    queue=deque([root])
    while queue:
        node=queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result[::-1]
n=int(input())
for _ in range(n):
    postfix=input()
    root=build_tree(postfix)
    result=level_traversal(root)
    print(''.join(result))