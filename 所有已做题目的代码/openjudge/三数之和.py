def find_triplets(nums):
    nums.sort()
    count=0
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==0:
                count+=1
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            elif total < 0:
                left+=1
            else:
                right-=1
    return count
nums=list(map(int, input().split()))
count=find_triplets(nums)
print(count)