class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def parse_tree(s):
    root=Treenode(s[0])
    current_node=root
    stack=[]
    for char in s[1:]:
        new_node=Treenode(char)
        if not current_node.left:
            current_node.left=new_node
            stack.append(current_node)
            current_node=new_node
        else:
            current_node.right=new_node
            current_node=new_node
        if char=='.' and stack:
            current_node=stack.pop()
    return root
def infix(root):
    if not root or root.value=='.':
        return []
    res=[]
    res+=infix(root.left)
    res.append(root.value)
    res+=infix(root.right)
    return res
def postfix(root):
    if not root or root.value=='.':
        return []
    res=[]
    res+=postfix(root.left)
    res+=postfix(root.right)
    res.append(root.value)
    return res
s=input()
root=parse_tree(s)
print(''.join(infix(root)))
print(''.join(postfix(root)))
    