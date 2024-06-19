class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
for _ in range(int(input())):
    n,m=map(int,input().split())
    nodes={i:Treenode(i) for i in range(n)}
    for i in range(n):
        X,Y,Z=map(int,input().split())
        if Y!=-1:
            nodes[X].left=nodes[Y]
            nodes[Y].parent=nodes[X]
        if Z!=-1:
            nodes[X].right=nodes[Z]
            nodes[Z].parent=nodes[X]
    for ii in range(m):
        operation=list(map(int,input().split()))
        if operation[0]==1:
            a,b=operation[1],operation[2]
            parent_1=nodes[a].parent
            parent_2=nodes[b].parent
            if parent_1==parent_2:
                parent_1.left,parent_1.right=parent_1.right,parent_1.left
            else:
                if parent_1.left==nodes[a]:
                    parent_1.left=nodes[b]
                else:
                    parent_1.right=nodes[b]
                if parent_2.left==nodes[b]:
                    parent_2.left=nodes[a]
                else:
                    parent_2.right=nodes[a]
                nodes[b].parent,nodes[a].parent=parent_1,parent_2
        else:
            c=operation[1]
            node=nodes[c]
            while node.left:
                node=node.left
            print(node.value)