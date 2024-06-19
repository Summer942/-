class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1
class AVLtree:
    def get_height(self,node): #获取树的高度
        if not node:
            return 0
        return node.height
    def get_balance_factor(self,node): #获取平衡因子
        if not node:
            return 0
        return self.get_height(node.left)-self.get_height(node.right)
    def right_rotate(self,lost_balance_node): #右旋操作
        new_node=lost_balance_node.left #失衡节点的左子节点成为新节点
        right_subtree=new_node.right #新节点的原右子树
        new_node.right=lost_balance_node #失衡节点作为新节点的右子节点
        lost_balance_node.left=right_subtree #新节点的右子树成为失衡节点的左子树
        lost_balance_node.height=1+max(self.get_height(lost_balance_node.left),self.get_height(lost_balance_node.right))
        new_node.height=1+max(self.get_height(new_node.left),self.get_height(new_node.right)) #更新高度
        return new_node
    def left_rotate(self,lost_balance_node): #左旋操作，与右旋相反
        new_node=lost_balance_node.right
        left_subtree=new_node.left
        new_node.left=lost_balance_node
        lost_balance_node.right=left_subtree
        lost_balance_node.height=1+max(self.get_height(lost_balance_node.left),self.get_height(lost_balance_node.right))
        new_node.height=1+max(self.get_height(new_node.left),self.get_height(new_node.right))
        return new_node
    def insert(self,node,key): #插入AVL树
        if not node:
            return Treenode(key)
        if node.val>key:
            node.left=self.insert(node.left,key)
        if node.val<key:
            node.right=self.insert(node.right,key)
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        balance_factor=self.get_balance_factor(node)
        if balance_factor>1 and key<node.left.val: #LL型失衡，右旋一次
            return self.right_rotate(node)
        if balance_factor<-1 and key>node.right.val: #RR型失衡，左旋一次
            return self.left_rotate(node)
        if balance_factor>1 and key>node.left.val: #LR型失衡，失衡节点的左子树左旋一次，然后整个树右旋一次
            node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance_factor<-1 and key<node.right.val: #RL型失衡，失衡节点右子树右旋一次，然后整个树左旋一次
            node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        return node
def preorder(node):
    if not node:
        return []
    res=[node.val]
    res+=preorder(node.left)
    res+=preorder(node.right)
    return res
avltree=AVLtree()
root=None
n=int(input())
keys=list(map(int,input().split()))
for key in keys:
    root=avltree.insert(root,key)
print(' '.join(map(str,preorder(root))))