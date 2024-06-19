def dfs(T,nums,i,res):
    if T==res:
        return True
    if i>=len(nums) or res>T:
        return False
    return dfs(T,nums,i+1,res*nums[i]) or dfs(T,nums,i+1,res)
T=int(input())
nums=list(map(int,input().split()))
if dfs(T,nums,0,1):
    print('YES')
else:
    print('NO')
