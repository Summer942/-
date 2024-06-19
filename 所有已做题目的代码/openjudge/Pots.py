from collections import deque
A,B,C=map(int,input().split())
def bfs(A,B,C):
    start=(0,0,[])
    queue=deque([start])
    visited=set()
    visited.add((0,0))
    while queue:
        a,b,ans=queue.popleft()
        if a==C or b==C:
            return ans
        operations=[(A,b,ans+['FILL(1)']),(a,B,ans+['FILL(2)']),\
                    (0,b,ans+['DROP(1)']),(a,0,ans+['DROP(2)']),\
                    (max(0,a+b-B),min(a+b,B),ans+['POUR(1,2)']),\
                    (min(A,a+b),max(0,a+b-A),ans+['POUR(2,1)'])]
        for operation in operations:
            new_state=(operation[0],operation[1])
            if new_state not in visited:
                visited.add(new_state)
                queue.append(operation)
    return 'impossible'
ans=bfs(A,B,C)
if ans=='impossible':
    print(ans)
else:
    print(len(ans))
    for _ in ans:
        print(_)
    