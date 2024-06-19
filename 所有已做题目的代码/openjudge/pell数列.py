n=int(input())
dp=[1]+[2]+[0]*148
for i in range(2,150):
    dp[i]=(2*dp[i-1]+dp[i-2])%32767
for ii in range(n):
    a=int(input())
    b=a%150
    print(dp[b-1])