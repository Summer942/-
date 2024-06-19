import heapq
graph={}
P=int(input())
for i in range(P):
    graph[input()]={}
Q=int(input())
for ii in range(Q):
    place_1,place_2,distance=input().split()
    graph[place_1][place_2]=int(distance)
    graph[place_2][place_1]=int(distance)
R=int(input())
for iii in range(R):
    start,end=input().split()
    heap=[]
    heapq.heappush(heap,(0,start,[start]))
    visited=set()
    while heap:
        total_distance,place,way=heapq.heappop(heap)
        if place==end:
            break
        visited.add(place)
        for next_place in graph[place]:
            heapq.heappush(heap,(total_distance+graph[place][next_place],next_place,\
                                 way+['('+format(str(graph[place][next_place]))+')']+[next_place]))
    print('->'.join(way))
            
