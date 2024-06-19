def build_tree(prefix,infix):
    if not prefix or not infix:
        return []
    root=prefix[0]
    root_index=infix.index(root)
    left_infix=infix[:root_index]
    right_infix=infix[root_index+1:]
    left_prefix=prefix[1:len(left_infix)+1]
    right_prefix=prefix[len(left_infix)+1:]
    tree=[]
    tree.extend(build_tree(left_prefix,left_infix))
    tree.extend(build_tree(right_prefix,right_infix))
    tree.append(root)
    return tree
while True:
    try:
        prefix,infix=input().split()
        print(''.join(build_tree(prefix,infix)))
    except EOFError:
        break