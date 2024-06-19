def monkey_king(n,m):
    if n==1:
        return 1
    else:
        x=0
        for i in range(2,n+1):
            x=(x+m)%i
        return x+1
while True:
    x,y=map(int,input().split())
    if x==0:
        break
    print(monkey_king(x, y))