n=int(input())
numbers=list(map(int,input().split()))
ans=[0]*n
stack=[]
for i in range(n-1,-1,-1):
    while stack and numbers[i]>=numbers[stack[-1]]:
        stack.pop()
    if stack:
        ans[i]=stack[-1]+1
    stack.append(i)
print(*ans)