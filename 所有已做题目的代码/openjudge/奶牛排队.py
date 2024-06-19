N=int(input())
cows=[int(input())for i in range(N)]
left_bound=[-1]*N
right_bound=[N]*N
stack=[]
for j in range(N):
    while stack and cows[j]>cows[stack[-1]]:
        stack.pop()
    if stack:
        left_bound[j]=stack[-1]
    stack.append(j)
stack=[]
for k in range(N-1,-1,-1):
    while stack and cows[stack[-1]]>cows[k]:
        stack.pop()
    if stack:
        right_bound[k]=stack[-1]
    stack.append(k)
ans=0
for i in range(N):
    for j in range(left_bound[i]+1,i):
        if right_bound[j]>i:
            ans=max(ans,i-j+1)
            break
print(ans)