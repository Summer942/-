n=int(input())
times=list(map(int,input().split()))
times.sort()
total_time=0
for i in range(n): 
    if total_time>times[i]:
       times[i]=0
    total_time+=times[i]
print(len(times)-times.count(0))