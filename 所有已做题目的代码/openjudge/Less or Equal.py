n,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
x=nums[k-1]
if k==n:
    print(nums[-1])
elif k==0:
    x=nums[0]-1
    if x>=1:
        print(x)
    else:
        print(-1)
else:
    if x==nums[k]:
        print(-1)
    else:
        print(x)