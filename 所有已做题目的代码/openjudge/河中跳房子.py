def check(stones,mid,M):
    removed=0
    basis=0
    for i in range(1,len(stones)):
        if stones[i]-basis<mid:
            removed+=1
        else:
            basis=stones[i]
    return removed<=M        
def max_min_distances(L,N,M,stones):
    left,right=0,L
    while left<right: 
        mid=(left+right+1)//2
        if check(stones,mid,M):
            left=mid
        else:
            right=mid-1
    return left
L,N,M=map(int,input().split())
stones=[0]+[int(input()) for i in range(N)]+[L]
print(max_min_distances(L, N, M, stones))

