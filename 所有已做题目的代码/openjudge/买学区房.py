import copy
n=int(input())
pairs=[i[1:-1] for i in input().split()]
distances=[sum(map(int,i.split(','))) for i in pairs]
prices=list(map(int,input().split()))
xingjiabi=[distances[ii]/prices[ii] for ii in range(n)]
prices_=copy.deepcopy(prices)
xingjiabi_=copy.deepcopy(xingjiabi)
prices.sort()
xingjiabi.sort()
if n%2==0:
    prices_medium=(prices[n//2-1]+prices[n//2])/2
    xingjiabi_medium=(xingjiabi[n//2-1]+xingjiabi[n//2])/2
else:
    prices_medium=prices[(n-1)//2]
    xingjiabi_medium=xingjiabi[(n-1)//2]
count=0
for iii in range(n):
    if xingjiabi_[iii]>xingjiabi_medium and prices_[iii]<prices_medium:
        count+=1
print(count)