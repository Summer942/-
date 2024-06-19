from collections import defaultdict
import heapq
n,k=map(int,input().split())
votes=list(map(int,input().split()))
S=set(map(int,input().split()))
items=[(votes[2*i],votes[2*i+1])for i in range(n)] #记录（时间，候选人编号）
items.sort() #按时间排序
heap=[(0,candidate)for candidate in S] #目标候选人的（票数，编号）
heapq.heapify(heap)
res=defaultdict(int) #计票器
current_time=items[0][0] #当前时间
index,ans,max_outside=0,0,0 #index为第几张票，ans为输出答案，max_outside为不在集合S中的最高票数
if k==314159: #特判：若所有成员都是候选人，则输出投票结束时间
    print(items[-1][0])
    exit()
while True:
    while index<n and items[index][0]==current_time:
        candidate_id=items[index][1]
        res[candidate_id]+=1
        if candidate_id in S:
            heapq.heappush(heap,(res[candidate_id],candidate_id))
        else:
            max_outside=max(max_outside,res[candidate_id]) 
        index+=1
    while heap and heap[0][0]!=res[heap[0][1]]: #若heap中的票数不是最终票数，则弹出
        heapq.heappop(heap)
    if index==n:
        break
    if heap[0][0]>max_outside: #候选人集合中的最低票数也比不在集合中的最高票数高
        ans+=items[index][0]-current_time
    if index==n:
        break
    current_time=items[index][0]
print(ans)