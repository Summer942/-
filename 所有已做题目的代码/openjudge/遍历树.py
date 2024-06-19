import heapq
class Treenode:
    def __init__(self,value):
        self.value=value
        self.child=[]
        self.parent=None
    def __lt__(self,other):
        return int(self.value)<int(other.value)
def build_tree(nodes):
    nodes_dict={}
    for node_values in nodes:
        parent_value=node_values[0]
        if parent_value not in nodes_dict:
            nodes_dict[parent_value]=Treenode(parent_value)
        parent_node=nodes_dict[parent_value]
        child_values=node_values[1:]
        for child_value in child_values:
            if child_value not in nodes_dict:
                nodes_dict[child_value]=Treenode(child_value)
            child_node=nodes_dict[child_value]
            child_node.parent=parent_node
            parent_node.child.append(child_node)
    for node in nodes_dict.values():
        if not node.parent:
            root=node
            break
    return root
def traversal(root,result):
    if not root.child:
        result.append(root.value)
        return
    children=root.child
    temp=[root]+children
    temp.sort()
    for child in temp:
        if child==root:
            result.append(root.value)
        else:
            traversal(child,result)
n=int(input())
nodes=[input().split() for i in range(n)]
root=build_tree(nodes)
result=[]
traversal(root,result)
for _ in result:
    print(_)