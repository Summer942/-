n,m=map(int,input().split())
goods=[list(map(int,input().split())) for i in range(n)]
coupons=[list(map(int,input().split('-'))) for ii in range(m)]
prices=0
for iii in range(n):
    prices+=goods[iii][1]
prices=prices-(prices//200)*30
for j in range(m):
    price=0
    for jj in range(n):
        if goods[jj][0]==j+1:
            price+=goods[jj][1]
    if price>=coupons[j][0]:
        prices=prices-coupons[j][1]
print(prices)