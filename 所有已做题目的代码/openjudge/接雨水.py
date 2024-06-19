n=int(input())
heights=list(map(int,input().split()))
left_bound=[-1]*n
right_bound=[-1]*n
stack=[]
for i in range(n):
    while stack and heights[stack[-1]]<=heights[i]:
        stack.pop()
    if stack:
        left_bound[i]=heights[stack[0]]
    stack.append(i)
stack=[]
for i in range(n-1,-1,-1):
    while stack and heights[stack[-1]]<=heights[i]:
        stack.pop()
    if stack:
        right_bound[i]=heights[stack[0]]
    stack.append(i)
rain=0
for j in range(n):
    if left_bound[j]>0 and right_bound[j]>0:
        rain+=min(left_bound[j],right_bound[j])-heights[j]
print(rain)