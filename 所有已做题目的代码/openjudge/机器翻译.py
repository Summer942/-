from collections import deque
M,N=map(int,input().split())
words=input().split()
queue=deque([])
count=0
for word in words:
    if word not in queue:
        if len(queue)==M:
            queue.popleft()
        queue.append(word)
        count+=1
print(count)