import copy
n=int(input())
pairs=[i[1:-1]for i in input().split()]
distances=[sum(map(int,i.split(','))) for i in pairs]
prices=list(map(int,input().split()))
xingjiabi=[distances[i]/prices[i]for i in range(n)]
xingjiabi_=copy.deepcopy(xingjiabi)
prices_=copy.deepcopy(prices)
xingjiabi_.sort()
prices_.sort()
if n%2==0:
    x=(xingjiabi_[n//2-1]+xingjiabi_[n//2])/2
    y=(prices_[n//2-1]+prices_[n//2])/2
else:
    x=xingjiabi_[(n-1)//2]
    y=prices_[(n-1)//2]
count=0
for i in range(n):
    if xingjiabi[i]>x and prices[i]<y:
        count+=1
print(count)