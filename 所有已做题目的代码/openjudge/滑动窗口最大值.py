from collections import deque
n,k=map(int,input().split())
nums=input().split()
maxs=[]
window=deque()
for i in range(n):
    if i>=k and window[0]==int(nums[i-k]):
        window.popleft()
    while window and window[-1]<int(nums[i]):
        window.pop()
    window.append(int(nums[i]))
    if i>=k-1:
        maxs.append(str(window[0]))
print(' '.join(maxs))