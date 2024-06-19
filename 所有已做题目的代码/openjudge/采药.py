T,M=map(int,input().split())
total_value=[0]*(T+1)
data=list(total_value)
for i in range(M):
    time,value=map(int,input().split())
    if time>T:
        continue
    else:
        for j in range(1,T+1):
            if j>=time:
                total_value[j]=max(data[j],value+data[j-time])
            else:
                total_value[j]=data[j]
        data=list(total_value)
print(data[-1])