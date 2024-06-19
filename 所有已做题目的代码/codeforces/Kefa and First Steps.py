n=int(input())
dp=[1]+[0]*(n-1)
sequence=list(map(int,input().split()))
for i in range(1,n):
    if sequence[i]>=sequence[i-1]:
        dp[i]=dp[i-1]+1
    else:
        dp[i]=1
print(max(dp))