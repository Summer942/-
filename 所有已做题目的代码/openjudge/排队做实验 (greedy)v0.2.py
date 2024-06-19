n=int(input())
times=list(map(int,input().split()))
items=[[times[i],i+1] for i in range(n)]
items.sort()
total=0
order=[]
for ii in range(n):
    total+=items[ii][0]*(n-1-ii)
    order.append(items[ii][1])
average=total/n
print(' '.join(map(str,order)))
print('{:.2f}'.format(average))