from collections import deque
while True:
    n=int(input())
    if n==0:
        break
    queue=deque(['1'])
    while queue:
        a=queue.popleft()
        if int(a)%n==0:
            break
        queue.append(a+'0')
        queue.append(a+'1')
    print(a)