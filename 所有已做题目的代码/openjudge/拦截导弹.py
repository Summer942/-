k=int(input())
heights=list(map(int,input().split()))
dp=[1]*k
for i in range(k-1,-1,-1):
    for j in range(i+1,k):
        if heights[j]<=heights[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))