from collections import defaultdict
n=int(input())
Graph=defaultdict(dict)
for _ in range(n-1):
    edges=input().split()
    start_vertex=edges[0]
    edge_num=int(edges[1])
    for i in range(1,edge_num+1):
        end_vertex=edges[2*i]
        weight=int(edges[2*i+1])
        Graph[start_vertex][end_vertex]=weight
        Graph[end_vertex][start_vertex]=weight
total_weight=0
visited=set('A')
while len(visited)<len(Graph):
    min_weight=float('inf')
    min_edge=None
    for node in visited:
        for edge in Graph[node]:
            if edge not in visited:
                if Graph[node][edge]<min_weight:
                    min_weight=Graph[node][edge]
                    min_edge=edge
    if min_edge:
        total_weight+=min_weight
        visited.add(min_edge)
print(total_weight)
            