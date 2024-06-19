n,m=map(int,input().split())
graph={i:[] for i in range(n)}
for j in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def is_connected(graph,n):
    visited=set()
    stack=[0]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return len(visited)==n        
def has_loop(graph):
    visited=set()
    stack=[(0,-1)]
    while stack:
        node,parent=stack.pop()
        if node in visited:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor!=parent:
                stack.append((neighbor,node))
    return False
if is_connected(graph,n):
    print('connected:yes')
else:
    print('connected:no')
if has_loop(graph):
    print('loop:yes')
else:
    print('loop:no')
        