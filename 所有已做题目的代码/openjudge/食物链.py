def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]
N,K=map(int,input().split())
parents=[0]*(3*N+1)
for i in range(3*N+1):
    parents[i]=i
ans=0
for _ in range(K):
    D,X,Y=map(int,input().split())
    if X>N or Y>N:
        ans+=1
        continue
    if D==1:
        if find(X+N)==find(Y) or find(Y+N)==find(X):
            ans+=1
            continue
        parents[find(X)]=find(Y)
        parents[find(X+N)]=find(Y+N)
        parents[find(X+2*N)]=find(Y+2*N)
    else:
        if find(X)==find(Y) or find(Y+N)==find(X):
            ans+=1
            continue
        parents[find(X+N)]=find(Y)
        parents[find(Y+2*N)]=find(X)
        parents[find(X+2*N)]=find(Y+N)
print(ans)
