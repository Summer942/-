class Vertex:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.neighbor=[]
    def add_neighbor(self,other):
        self.neighbor.append(other)
class Graph:
    def __init__(self,weights):
        self.graph=[Vertex(i,weights[i])for i in range(len(weights))]
    def add_edge(self,a,b):
        self.graph[a].add_neighbor(b)
        self.graph[b].add_neighbor(a)
def total_weight(i,graph,visited):
    if visited[i]:
        return 0
    total=weights[i]
    visited[i]=True
    if graph.graph[i].neighbor:
        for j in graph.graph[i].neighbor:
            total+=total_weight(j,graph,visited)
    return total   
n,m=map(int,input().split())
weights=list(map(int,input().split()))
graph=Graph(weights)
visited=[False]*n
for _ in range(m):
    a,b=map(int,input().split())
    graph.add_edge(a,b)
max_total_weight=0
for i in range(n):
    total=total_weight(i,graph,visited)
    max_total_weight=max(total,max_total_weight)
print(max_total_weight)