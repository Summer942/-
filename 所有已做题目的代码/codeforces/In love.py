from collections import defaultdict
from heapq import heappush, heappop
q=int(input())
l,r=[],[]
left,right=defaultdict(int),defaultdict(int)
for _ in range(q):
    operation,a,b=input().split()
    a,b=int(a),int(b)
    if operation=='+':
        heappush(l,-a) 
        heappush(r,b) 
        left[a]+=1
        right[b]+=1
    else: 
        left[a]-=1 
        right[b]-=1
    while l and left[-l[0]]<=0: 
        heappop(l)
        heappop(r)
    while r and right[r[0]]<=0: 
        print('YES' if l and r and -l[0]>r[0] else 'NO')