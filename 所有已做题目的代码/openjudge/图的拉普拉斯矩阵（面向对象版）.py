class Vertex:
    def __init__(self,value):
        self.value=value
        self.neighbor=[]
    def add_neighbor(self,other):
        self.neighbor.append(other)
class Graph:
    def __init__(self,n):
        self.graph=[Vertex(_)for _ in range(n)]
    def add_edge(self,a,b):
        self.graph[a].add_neighbor(b)
        self.graph[b].add_neighbor(a)
    def laplacian_matrix(self):
        n=len(self.graph)
        matrix=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    matrix[i][j]=len(self.graph[i].neighbor)
                elif j in self.graph[i].neighbor:
                    matrix[i][j]=-1
        return matrix
n,m=map(int,input().split())
graph=Graph(n)
for _ in range(m):
    a,b=map(int,input().split())
    graph.add_edge(a,b)
matrix=graph.laplacian_matrix()
for _ in matrix:
    print(*_)