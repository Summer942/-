n=int(input())
nums=list(map(int,input().split()))
nums.sort()
ans1=[]
ans2=[]
for i in range(1,n+1):
    if i not in nums:
        ans1.append(i)
for num in nums:
    if num>n:
        ans2.append(num)
print(' '.join(map(str,ans1)))
print(' '.join(map(str,ans2)))
    