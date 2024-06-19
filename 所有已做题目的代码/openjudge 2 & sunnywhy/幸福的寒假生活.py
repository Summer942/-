def function(month,day):
    if month==1:
        return day-6
    else:
        return day+25
n=int(input())
plans=[]
for _ in range(n):
    start,end,value=input().split()
    month1,day1=map(int,start.split('.'))
    month2,day2=map(int,end.split('.'))
    start=function(month1,day1)
    end=function(month2,day2)
    plans.append([start,end,int(value)])
dp=[0]*46
for i in range(1,46):
    dp[i]=dp[i-1]
    for start,end,value in plans:
        if end==i:
            dp[i]=max(dp[start-1]+value,dp[i])
print(dp[-1])
