dp=[0]*31
dp[0]=0
dp[1]=dp[2]=1
for i in range(3,31):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
n=int(input())
print(dp[n])