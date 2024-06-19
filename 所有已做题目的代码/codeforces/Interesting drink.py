n=int(input())
shops=list(map(int,input().split()))
shops.sort()
q=int(input())
for i in range(q):
    money=int(input())
    count=0
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if money>=shops[mid]:
            count=mid+1
            left=mid+1
        else:
            right=mid-1
    print(count)