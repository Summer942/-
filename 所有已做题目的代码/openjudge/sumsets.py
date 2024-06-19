import math
power_of_2=[0]+[2**i for i in range(20)]
N=int(input())
n=int(math.log(N,2))+1
dp=[1]+[0]*N
for i in range(1,n+1):
    for j in range(power_of_2[i],N+1):
        dp[j]=(dp[j]+dp[j-power_of_2[i]])%(10**9)
print(dp[-1])