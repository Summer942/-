while True:
    try:
        N=int(input())
        graph={}
        for i in range(N):
            distances=list(map(int,input().split()))
            graph[i+1]={}
            for j,distance in enumerate(distances):
                if j!=i:
                     graph[i+1][j+1]=distance
        total=0
        visited=set()
        visited.add(1)
        while len(visited)<len(graph):
            min_distance=float('inf')
            min_farm=None
            for farm in visited:
                for next_farm in graph[farm]:
                    if next_farm not in visited:
                        if graph[farm][next_farm]<min_distance:
                            min_distance=graph[farm][next_farm]
                            min_farm=next_farm
            if min_farm:
                total+=min_distance
                visited.add(min_farm)
        print(total)
    except EOFError:
        break