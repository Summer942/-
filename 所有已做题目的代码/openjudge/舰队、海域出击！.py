from collections import defaultdict,deque
def has_loop(graph):
    queue=deque([])
    for i in range(1,N+1): 
        if in_degrees[i]==0:
            queue.append(i)
    while queue:
        node=queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            in_degrees[neighbor]-=1
            if in_degrees[neighbor]==0:
                queue.append(neighbor)
    return N!=len(visited)
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    graph=defaultdict(list)
    in_degrees=[0]*(N+1)
    visited=set()
    for _ in range(M):
        x,y=map(int,input().split())
        graph[x].append(y)
        in_degrees[y]+=1
    if has_loop(graph):
        print('Yes')
    else:
        print('No')
    
        
        