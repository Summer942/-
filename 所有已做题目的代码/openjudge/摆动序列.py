n=int(input())
nums=list(map(int,input().split()))
if n==1:
    print(1)
else:
    minus1=nums[1]-nums[0]
    if minus1!=0:
        ans=2
    else:
        ans=1
    for i in range(2,n):
        minus2=nums[i]-nums[i-1]
        if minus1*minus2<0:
            ans+=1
            minus1=minus2
print(ans)
            