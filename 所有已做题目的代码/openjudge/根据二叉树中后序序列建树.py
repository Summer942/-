def build_tree(inorder,postorder):
    if not inorder or not postorder:
        return []
    root=postorder[-1] #后序表达式的最后一个一定为根节点
    root_index=inorder.index(root)
    left_inorder=inorder[:root_index] #左子树的中序表达式
    right_inorder=inorder[root_index+1:] #右子树的中序表达式
    left_postorder=postorder[:len(left_inorder)] #左子树的后序表达式
    right_postorder=postorder[len(left_inorder):-1] #右子树的后序表达式
    tree=[root]
    tree.extend(build_tree(left_inorder,left_postorder)) #将左子树视为一个新的二叉树，递归
    tree.extend(build_tree(right_inorder,right_postorder)) #将右子树视为一个新的二叉树，递归
    #注意：根据前序遍历的要求，左子树先右子树后
    return tree
inorder=input()
postorder=input()
preorder=build_tree(inorder, postorder)
print(''.join(preorder))