class Treenode:
    def __init__(self,value):
        self.value=value
        self.children=[]
def parse_tree(s):
    stack=[] #储存双亲节点
    for char in s:
        if char.isalpha(): #是字母，创建节点
            node=Treenode(char)
            if stack: #栈非空，则当前节点一定是栈顶节点的孩子节点
                stack[-1].children.append(node)
        if char=='(': #是(，则当前节点可能是双亲节点
            stack.append(node)
        if char==')': #是),则栈顶节点的孩子节点已全部列出
            node=stack.pop()
    return node #返回根节点
def preorder(node):
    output=[node.value]
    for child in node.children:
        output.extend(preorder(child))
    return ''.join(output)
def postorder(node):
    output=[]
    for child in node.children:
        output.extend(postorder(child))
    output.append(node.value)  #所有孩子节点输出之后在输出双亲节点
    return ''.join(output)
s=input()
root=parse_tree(s)
print(preorder(root))
print(postorder(root))