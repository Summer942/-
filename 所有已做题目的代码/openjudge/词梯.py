from collections import deque
def build_graph(words):
    graph={}
    for word in words:
        for i in range(4):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket not in graph:
                graph[bucket]=[]
            graph[bucket].append(word)
    return graph
def bfs(start,end,graph):
    queue=deque([(start,[start])])
    visited=set(start)
    while queue:
        word,path=queue.popleft()
        if word==end:
            return path
        for i in range(4):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in graph:
                neighbors=graph[bucket]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,path+[neighbor]))
    return None
n=int(input())
words=[]
for i in range(n):
    words.append(input())
start,end=input().split()
graph=build_graph(words)
path=bfs(start,end,graph)
if path:
    print(' '.join(path))
else:
    print('NO')
                    