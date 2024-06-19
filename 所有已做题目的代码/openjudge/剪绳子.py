import heapq
N=int(input())
lengths=list(map(int,input().split()))
heapq.heapify(lengths)
ans=0
for i in range(N-1):
    a=heapq.heappop(lengths)
    b=heapq.heappop(lengths)
    c=a+b
    ans+=c
    heapq.heappush(lengths, c)
print(ans)