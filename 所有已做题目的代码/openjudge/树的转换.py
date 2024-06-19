class Treenode:
    def __init__(self,value):
        self.value=value
        self.children=[]
        self.left=None
        self.right=None
def parse_tree(s):
    root=Treenode(0)
    current_node=root
    stack=[]
    value=0
    for char in s:
        if char=='d':
            value+=1
            new_node=Treenode(value)
            current_node.children.append(new_node)
            stack.append(current_node)
            current_node=new_node
        else:
            current_node=stack.pop()
    return root
def original_height(root):
    if not root.children:
        return 0
    max_height=0
    for child in root.children:
        max_height=max(max_height,original_height(child)+1)
    return max_height
def convert_to_binary_tree(root):
    binary_root=root
    if root.children:
        binary_root.left=convert_to_binary_tree(root.children[0])
    current_node=binary_root.left
    for child in root.children[1:]:
        current_node.right=convert_to_binary_tree(child)
        current_node=current_node.right
    return binary_root
def converted_height(root):
    if not root:
        return -1
    return max(converted_height(root.left),converted_height(root.right))+1
s=input()
root=parse_tree(s)
original=original_height(root)
binary_root=convert_to_binary_tree(root)
converted=converted_height(binary_root)
print(f"{original} => {converted}")
        