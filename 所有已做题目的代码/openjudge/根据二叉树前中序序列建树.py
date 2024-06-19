def build_tree(preorder,inorder):
    if not preorder or not inorder:
        return []
    root=preorder[0]
    root_index=inorder.index(root)
    left_inorder=inorder[:root_index]
    right_inorder=inorder[root_index+1:]
    left_preorder=preorder[1:len(left_inorder)+1]
    right_preorder=preorder[len(left_inorder)+1:]
    tree=[]
    tree.extend(build_tree(left_preorder,left_inorder))
    tree.extend(build_tree(right_preorder,right_inorder))
    tree.append(root)
    return tree
while True: 
    try:
        preorder=input()
        inorder=input()
        print(''.join(build_tree(preorder,inorder)))
    except EOFError:
        break