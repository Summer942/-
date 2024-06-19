def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]
def union(x,y):
    parents[find(y)]=find(x)
while True:
    try:
        n,m=map(int,input().split())
        parents=[i for i in range(n+1)]
        for _ in range(m):
            x,y=map(int,input().split())
            if find(x)==find(y):
                print('Yes')
            else:
                print('No')
                union(x, y)
        res=set(find(x) for x in range(1,n+1))
        num=len(res)
        print(num)
        print(' '.join(map(str,sorted(res))))
    except EOFError:
        break