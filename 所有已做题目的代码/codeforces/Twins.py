num=int(input())
coins=input().split()
coin=[]
for i in range(num):
    coin.append(int(coins[i]))
s=sum(coin)
x=0
y=0
while x<=(s-x):
    a=max(coin)
    x=x+a
    b=coin.index(a)
    del coin[b]
    y+=1
print(y)

