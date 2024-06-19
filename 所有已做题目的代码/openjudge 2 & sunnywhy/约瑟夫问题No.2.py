from collections import deque 
while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    ring=deque([i for i in range(1,n+1)])
    while ring[0]!=p:
        left=ring.popleft()
        ring.append(left)
    ans=[]
    count=1
    while ring:
        left=ring.popleft()
        if count==m:
            ans.append(left)
            count=0
        else:
            ring.append(left)
        count+=1
    print(','.join(map(str,ans)))