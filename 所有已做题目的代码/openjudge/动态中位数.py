import heapq
T=int(input())
for _ in range(T):
    ans=[]
    min_heap=[]
    max_heap=[]
    nums=list(map(int,input().split()))
    for i in range(len(nums)):
        if not max_heap or nums[i]>max_heap[0]:
            heapq.heappush(max_heap,nums[i])
        else:
            heapq.heappush(min_heap,-nums[i])
        if len(max_heap)>len(min_heap)+1:
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        elif len(min_heap)>len(max_heap):
            heapq.heappush(max_heap,-heapq.heappop(min_heap))
        if i%2==0:
            ans.append(max_heap[0])
    print(len(ans))
    print(*ans)
        