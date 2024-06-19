from collections import deque
t=int(input())
for i in range(t):
    n=int(input())
    permutation=deque(map(int,input().split()))
    permutation_=sorted(permutation)
    x,y=1,n
    try: 
        a,b=0,n-1
        while permutation[0]==permutation_[a] or permutation[0]==permutation_[b]\
           or permutation[-1]==permutation_[a] or permutation[-1]==permutation_[b]: 
                  if permutation[0]==permutation_[a]: 
                      permutation.popleft()
                      a+=1
                      x+=1
                  if permutation[0]==permutation_[b]:
                      permutation.popleft()
                      b-=1
                      x+=1
                  if permutation[-1]==permutation_[a]:
                      permutation.pop()
                      a+=1
                      y-=1
                  if permutation[-1]==permutation_[b]:
                      permutation.pop()
                      b-=1
                      y-=1
    except: 
        print(-1)
    if x<y:
        print(x,y)
        
   