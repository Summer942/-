n,t=map(int,input().split())
prices=list(map(int,input().split()))
total=sum(prices)
if total<t:
    print(0)
else:
    dp=[0]*(total+1) #dp[i]表示总价为i时有几种凑单方法
    dp[0]=1 #总价为0，即什么都不买，只有这1种凑单方法
    for price in prices: 
        for i in range(total,price-1,-1):
            dp[i]+=dp[i-price] #总价等于（i-该商品的单价）有几种凑单方法，总价等于i就有几种凑单方法
    for ii in range(t,total+1):
        if dp[ii]>0: #大于等于t时有凑单方法
            print(ii)
            break