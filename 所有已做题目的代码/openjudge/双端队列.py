from collections import deque
t=int(input())
for i in range(t):
    n=int(input())
    queue=deque()
    for ii in range(n):
        a,b=map(int,input().split())
        if a==1:
            queue.append(b)
        else:
            if queue:
                if b==0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                break
    if len(queue)!=0:
        print(' '.join(map(str,list(queue))))
    else:
        print('NULL')