from collections import defaultdict
import heapq
K=int(input())
N=int(input())
R=int(input())
graph=defaultdict(list)
for _ in range(R):
    S,D,L,T=map(int,input().split())
    graph[S].append((D,L,T))
visited=set()
start=(0,0,1)
heap=[]
heapq.heappush(heap,start)
while heap:
    total_length,total_charge,current_city=heapq.heappop(heap)
    if (current_city,total_charge) in visited:
        continue
    visited.add((current_city,total_charge))
    if current_city==N:
        print(total_length)
        break
    for next_city,next_length,next_charge in graph[current_city]:
        if total_charge+next_charge<=K:
            heapq.heappush(heap,(total_length+next_length,total_charge+next_charge,next_city))
if current_city!=N:
    print(-1)    